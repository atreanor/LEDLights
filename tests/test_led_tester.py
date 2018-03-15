# tests/test_led_tester.py
import sys
sys.path.append('.')

import pytest
from LightTester import *


def test_command_line_interface():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None
    
def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 
                            'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 
                            'turn on 2,2 through 7,7\n']

def test_instruction_parsing():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert cmd == "turn on" or cmd == "turn off" or cmd == "switch"
    
  
def test_coord_outside_parameters():
    lights = LightTest(5)
    lights.apply("turn on 0,0 through 10,11")
assert ledTester.count() == 25

def test_count():
    lights = LightTest(10)
    lights.apply("turn on 0,0 through 9,9")
    assert lights.count() == 100
    
    
     