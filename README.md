## Benchmarking for different types of protrein file formats 
This repository contains the python script that benchmarks different protein file formats for parsing speed comparison. The results were used in the paper **"MMTF - an efficient file format for the transmission, visualization, and analysis of macromolecular structures"**. The repository also contains some csv files which includes lists of proteins in the same range of sizes, along with the largest known protein structure *3J3Q*. 

## Outputs and locations
The python script will download and parse all proteins from each csv files, and return the download time in *downdload_benchmarks_results.csv*, and the parsing time *parsing_benchmark_results.csv*. All protein will be sorted into **/pdb**, **/cif** or **/mmtf** folder depending on their file type. Fast_cif is a way to parse mmcif files, so there will not be any fast_cif files. All files and outputs will be stored in the current work directory.

## Version requirements
This script requires **Python 3.x**. You can download python from:

*https://www.python.org/downloads/* 

or 

*https://www.continuum.io/downloads*


## Installing required python packages
The python script in this repository requires a few packages, including *biopython* and *wget*. These packages can be installed through pip: 
```
pip install biopython 
pip install wget 
pip install gzip
``` 

## How to run the program
To run the benchmark, you have to get the lastest source code from git, then excute your python file in terminal or command line:
```
$ git clone https://github.com/altaite/mmtf-python-benchmark.git
$ python benchmark_mmtf_python.py
``` 
