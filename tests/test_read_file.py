# tests/test_read_file.py
import sys
sys.path.append('.')

import pytest
from LightTester import LightTest
from LightTester import utils

def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 
    'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 
    'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7\n']
      