'''
@author: aonghus
'''
import requests
from pathlib import Path
import re
import urllib.request
#import req

#import urllib2

#sys.path.append(".")




def parseFile1(input):
    #read from http uri
    pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")   
    if input.startswith("http"):
        print('http')
        N, instructions = None, []
        uri = input
        r = requests.get(uri).text
        instructions = r.splitlines()
        fout = open('output.txt', 'w')
        fout = instructions 
        #for line in instructions:
        #    fout.write(line)
        print(fout) 
        
        #print(instructions)
        #N = int(instructions[0])
        #for i in range
        #newtextfile = str(newtextfile)
        #for i in range(1, len(newtextfile)):
        #    instructions.append(newtextfile[i])
            
        parsehttp(fout)
    

    my_file = Path(input)
    if my_file.is_file():
        print('local')
        # read from file
        N, instructions = None, []
        
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                if re.search(pat, line):
                    result = re.search(pat, line)
                instructions.append(result.group(1, 2, 3, 4, 5))
        print('local file executed')
        print(N, instructions)
        return N, instructions
    else:
        print('nothing executed')
    return
    #unable to read file
    #re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
def parsehttp(input):
    pat = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
    N, instructions = None, []
    with open(input, 'r') as f:
        N = int(f.readline())
        for line in f.readlines():
            if re.search(pat, line):
                result = re.search(pat, line)
            instructions.append(result.group(1, 2, 3, 4, 5))
        print(N, instructions)
        return N, instructions
#parseFile('')   
parseFile1('test_data.txt')   
#parseFile('http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt') 

