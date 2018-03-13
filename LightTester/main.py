# LightTester/main.py
import sys
sys.path.append(".")

import argparse
from utils import * 
from LightTest import *
import urllib.request 
import os
import re
from pprint import pprint
import pytest

def main():
    '''main method'''
    print('main method entered')
    #N, instructions = None, []
    
    # read input from web or local file
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input
    print('1: file read')
    
    # parse file to obtain N, instructions 
    N, instructions = parseFile(filename)
    print('2: file parsed & regexed')
    
    # create instance of class, N = 2d dimensions
    lights = LightTest(N)
    print('3: class created')
    
    #pprint(LightTest)
    lights.apply(instructions)
    print('instructions applied')
    
    #count and print lights on   
    print("Lights on: ", lights.count())
    return 0

if __name__ == "__main__":
    main()
    #sys.exit(main()) # pragma: no cover 
    
