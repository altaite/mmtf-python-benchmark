# Benchmarks for comparing 3D structure file parser performance in Biopython
 
This repository contains **Python 3.x** code for comparing the file parsing performance of the PDB and PDBx/mmCIF *(https://www.wwpdb.org/documentation/file-format)* file formats with the new MacroMolecular Transmission Format *(MMTF, http://mmtf.rcsb.org)* using the following Biopython parsers: *MMCIFParser, FastMMCIFParser, PDBParser, and MMTFParser*. The results of these benchmarks are described in the paper: **MMTF - an efficient file format for the transmission, visualization, and analysis of macromolecular structures (2017) bioRxiv 122689,  https://doi.org/10.1101/122689.**

This repository also contains benchmark datasets: **sample_1000.csv** is a set of 1000 randomly selected PDB structures, **sample_25.csv, sample_50.csv, sample_75.csv** contain 100 structures each around the 25, 50 and 75 percentile of the PDB size distribution: Q25 (2,309-2,313 atoms), Q50 (4,054-4,063 atoms), Q75 (7,862-7,885 atoms), **sample_3j3q.csv** contains the largest structure in the PDB.

## Outputs and locations
The Python script will download and parse all proteins from each csv files, and return the download time in **downdload_benchmark_results.csv**, and the parsing time **parsing_benchmark_results.csv**. Downloaded structures will be saved into */pdb*, */cif* or */mmtf* folder depending on their file type.

## Version requirements
This script requires **Python 3.x**. You can download the latest Python versions from:

*https://www.python.org/downloads/* 

or 

*https://www.continuum.io/downloads*


## Installing required python packages
The Python script in this repository requires a few packages, including *biopython* and *wget*. These packages can be installed through pip: 
```
pip install biopython 
pip install wget 
pip install gzip
``` 

## How to run the program
To run the benchmark, you have to get the lastest source code from git, then excute your Python file in terminal or command line:
```
$ git clone https://github.com/altaite/mmtf-python-benchmark.git
$ python benchmark_mmtf_python.py
``` 
