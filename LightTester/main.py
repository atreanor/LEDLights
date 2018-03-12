sys.path.append(".")
import sys
import argparse
from utils import * 
import urllib.request 
import os
import re
import pytest



def main():
    '''main method'''
    
    # read input from web or local file
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    filename = args.input
    
    N,instructions = parseFile(filename)
    
    # create instance of class, N = 2d dimensions
    lights = LightTest(N)
    
    
    # parse input with regex, output N & instructions
    N, instructions = parseFile(input)
    
    #create 2d list of N dimensions
    ledTester = LightTest(N)
    pprint(lights)
    
    #read instructions and invoke apply
    for cmd in instructions:
        self.apply(instruction)
    
    
    
    #count and print lights on   
    print("Lights on: ", lights.count())
    return 0


if __name__ == "__solve_led__":
    sys.exit(main()) # pragma: no cover 

