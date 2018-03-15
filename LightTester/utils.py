# LightTester/utils.py
import sys 
sys.path.append(".")
import urllib.request
import re 
import os

def parseFile(input):
    ''' method to parse http/local file to executable instructions '''
        
    if input.startswith('http'):
        req = urllib.request.urlopen(input)
        # read the whole file into a buffer
        buffer = req.read().decode('utf-8').split('\n')
        N = int(buffer[0])
        instructions = regexConvert(buffer)
        print('2: http file parsed')
        return N, instructions
    else:
        # check if file exists
        if os.path.isfile(input):
            # read whole file to buffer
            buffer = open(input).read().split("\n")
            N = int(buffer[0])
            #print('Buffer', buffer)
            instructions = regexConvert(buffer)
            #N, instructions = None, []
            print('2: local file parsed')
            return N, instructions 
        else:
            print('Error: file not found')
            return 0,0
    

def regexConvert(buffer):
    ''' method to convert buffer file data with regular expression to executable file '''
    
    
    instructions = []
    for i in range(1, len(buffer)):
        regex = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
                
        regexLine = regex.match(buffer[i])
        if regexLine:
            r = list(regexLine.groups())
            for i in range(1,5):
                r[i] = int(r[i])
            instructions.append(r)

    return instructions
   
    
    