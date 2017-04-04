import random
import os
from timeit import default_timer as timer
import gzip
try:
    from Bio.PDB import FastMMCIFParser
    from Bio.PDB import MMCIFParser
    from Bio.PDB import PDBParser
    from Bio.PDB.mmtf import MMTFParser
    from Bio.PDB import PDBList
except Exception: 
    print("please have Biopython installed (eg: pip install biopython)")
try: 
    import wget
except Exception: 
    print("please have wget installed (eg: pip install wget)") 


#all files to test
#infiles = ['sample_3j3q.csv','sample_25.csv','sample_50.csv','sample_75.csv','sample_1000.csv']
infiles = ['sample_25.csv']

#3 types of files and the "FastMMCIFParser" to be tested
file_types = ['mmtf','cif','fast_cif' ,'pdb']

'''
funtion that reads protein list file and store in a list
*takes file with list of protein as input 
'''
get_proteins = lambda x: [p[:4].upper() for p in open(x,'r')]


'''
download all proteins from the sample protein listin all 3 formats from pdb and store in local directories
* file_type: the type of file to be downloaded (mmtf, pdb, mmcif)
* all_proteins: the list of all proteins to be downloaded
'''
def get_all_protein(file_type,proteins):
    #iterate over all proteins and download their mmtf files 
    if file_type == 'fast_cif': file_type = 'cif'
    for protein in proteins:
        if file_type == 'pdb' and protein == '3J3Q':
            print("\n 3j3q not in pdb website")
            continue    
        if file_type == 'mmtf': 
            url = "http://mmtf.rcsb.org/v1.0/full/%s.mmtf.gz"%(protein)
            filename = "%s.mmtf.gz"%(protein)
        elif file_type == 'cif': 
            url = "https://files.rcsb.org/download/%s.cif.gz"%(protein)
            filename = "%s.cif.gz"%(protein)
        else: 
            url = "https://files.rcsb.org/download/%s.pdb.gz"%(protein)
            filename = "%s.pdb.gz"%(protein)
        wget.download(url)
        #uncompress gzipped file to file 
        infile = gzip.open(filename,'rb')
        outfile = open(filename[:-3],'wb')
        outfile.write(infile.read())
        infile.close()
        outfile.close()
        cwd = os.getcwd()
        os.remove(cwd + '/' + filename)
        #sort proteins into directories by their middle two characters
        directory = "%s/%s"%(cwd,file_type)
        if not os.path.exists(directory):
            os.makedirs(directory)
        if not os.path.exists("%s/%s.%s"%(directory,protein,file_type)):
            os.rename("%s/%s.%s"%(cwd,protein,file_type),\
            "%s/%s.%s"%(directory,protein,file_type))
        else:
            os.remove("%s/%s.%s"%(cwd,protein,file_type))


'''
Time download for each file type
*takes a list of protein as input
'''
def time_download(infile,proteins):
    time_keeper = []
    for file_type in file_types:
        if file_type == 'fast_cif': continue
        begin = timer()
        get_all_protein(file_type,proteins)
        terminal  = timer()
        result = "download all %s files took %f seconds"%(file_type,terminal-begin)
        time_keeper.append(result)
    #write benchmark results to text file
    with open("download_benchmark_results.csv","w") as o:
        for t in time_keeper: 
            o.write(t + '\n')


'''
Get parsing time for all proteins in protein list for specific format
Parameters: 
* file_type: the type of file to be parsed (mmtf, pdb, mmcif)
* proteins: the list of proteins to be parsed
* rep: number of repetition each protein is timed (default to 10)
'''
def loop_parsing(file_type,proteins,rep = 10):
    cwd = os.getcwd()
    if file_type == 'mmtf': parser = MMTFParser()
    elif file_type == 'fast_cif': parser = FastMMCIFParser()
    elif file_type == 'cif': parser = MMCIFParser()
    else: parser = PDBParser()
    for p in proteins:
        if file_type == "fast_cif": file_type = "cif"
        directory = "%s/%s/%s.%s"%(cwd,file_type,p,file_type)
        try: 
            if file_type == 'mmtf':
                protein = parser.get_structure(directory)
            else:
                protein = parser.get_structure(random.randint(0,100),directory)
        except Exception: 
            print("Having trouble parsing %s"%(p))
            break
    return


'''
Generates timing_results.txt which contains:
* takes a list of protein as input
* total parsing time for each format
'''
def time_parsing(proteins):
    total_time = {}
    #iterate and time all filetypes
    for file_type in file_types:
        begin = timer()
        loop_parsing(file_type,proteins)
        terminal = timer ()
        total_time[file_type] = terminal-begin
    return total_time


'''
Main funciton for benchmark
'''
if __name__ == '__main__': 
    infile_time = {}
    #loop over all files and benchmark 
    for f in infiles:
        proteins = get_proteins(f)
        time_download(f,proteins)
        infile_time[f] = time_parsing(proteins)
    #write benchmark results to text file
    with open("parsing_benchmark_results.csv","w") as o:
        o.write("File,MMTF,MMCIF,FastMMCIF,PDB \n")
        for f in infiles: 
            o.write(f[:-4] + "," + str(infile_time[f]["mmtf"])+","+str(infile_time[f]["cif"])+ \
            "," + str(infile_time[f]["fast_cif"])+","+ str(infile_time[f]["pdb"]) + "\n")
