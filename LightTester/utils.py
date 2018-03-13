# LightTester/utils.py
import sys 
sys.path.append(".")
import urllib.request
#help(urllib.request.urlopen)
#from pathlib import Path
import re 
import os

def parseFile(input):
    
    if input.startswith('http'):
        # N, instructions = None, []
        req = urllib.request.urlopen(input)
        # read the whole file into a buffer
        buffer = req.read().decode('utf-8').split('\n')
        N = int(buffer[0])
        print('Buffer', N, buffer)
        instructions = regexConvert(buffer)
        print('http file read')
        return N, instructions
    else:
        # check if file exists
        if os.path.isfile(input):
            print('local file exits')
            # read whole file to buffer
            buffer = open(input).read().split("\n")
            N = int(buffer[0])
            #print('Buffer', buffer)
            instructions = regexConvert(buffer)
            #N, instructions = None, []
            print('local file read')
            return N, instructions 
        else:
            print('Error: file not found')
            return 0,0
    

def regexConvert(buffer):
    # convert buffer data with regex 
    
    instructions = []
    for i in range(1, len(buffer)):
        regex = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        #result = re.search(regex)
        #instructions.append(result.group(1, 2, 3, 4, 5))
        
        regexLine = regex.match(buffer[i])
        if regexLine:
        #regexLine1 = regexLine.group(1, 2, 3, 4, 5)
        # append data
            r = list(regexLine.groups())
            for i in range(1,5):
                r[i] = int(r[i])
            # r = [regexLine.group(x) for x in [1, 2, 3, 4, 5]]
            instructions.append(r)
        #print(instructions)
    return instructions
  

'''def coordCheck(self, x1, y1, x2, y2):
    if x1 < 0:
        x1 = 0
    if y1 < 0:
        y1 = 0
    if x2 > self.size:
        x2 = self.size
    if y2 > self.size:
        y2 = self.size 
'''        
        
#parseFile('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt')
#parseFile('input_assign3.txt')
#parseFile('')
    
    
    