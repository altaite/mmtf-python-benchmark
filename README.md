## Benchmarking for different types of protrin file formats 
This repository contains the python script that benchmarks different protein file formats for parsing speed comparison. The results were used in the paper **"MMTF - an efficient file format for the transmission, visualization, and analysis of macromolecular structures"**. The repository also contains some csv files which includes lists of proteins in the same range of sizes, along with the largest know protein *3J3Q*. The python script will download and parse all proteins from each csv files, and return the download time in *downdload_benchmarks_results.csv*, and the parsing time *parsing_benchmark_results.csv*. 

## Installing required python packages
The python script in this repository requires a few packages, including *biopython* and *wget*. These packages can be installed through pip: 
'''
pip install biopython
pip install wget 
pip install gzip
''' 

## How to run the program
To run the benchmark, you have to get the lastest source code from git, then excute your python file in terminal or command line:
'''
$ git clone https://github.com/altaite/mmtf-python-benchmark.git
$ python benchmark_mmtf_python.py
''' 
