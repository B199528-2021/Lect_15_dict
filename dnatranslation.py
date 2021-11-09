#!/usr/local/bin/python3

import os
import sys
import subprocess
import shutil

dnasequence = "ACCTGCGGAAGGATCATTACCGAGTGCGGGTCCTTTGGGCCCAACCTCCCATCCGTGTCTATTGT"

with open("gencode.txt") as gencode:
    gencode = gencode.read().upper()

for index,base in enumerate(dnasequence):
    
    # get every third base 
    if index % 3 == 0:
        print(index, base)
        # get three bases
        try:
            print(dnasequence[index:index+3])
        # there will be an index error at the end of the sequence
        except IndexError:
            continue
    # print(index)
    # print(base)

exit()

for index in range (0, len(dnasequence), 3):
    print(index)
