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
import time 


def main():
    '''main method: entry point of package. reads input from console, parses the data, applies
    instructions to grid, counts result & times execution'''
    start_time = time.time()
        
    # read input from web or local file
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input
    print('1: console input received')
    
    # parse file to obtain N, instructions 
    N, instructions = parseFile(filename)
    
    
    # create instance of class, N = 2d dimensions
    lights = LightTest(N)
    print('3: class instance created')
    
    #pprint(LightTest)
    lights.apply(N, instructions)
    print('4: instructions applied')
    
    #count and print lights on   
    print("5: lights on: ", lights.count())
    print("--- %s mins -" % int((time.time() - start_time)/60) + "-- %s secs ---" % int(time.time() - start_time))
    return 0

if __name__ == "__main__":
    #main()
    sys.exit(main()) # pragma: no cover 
    
