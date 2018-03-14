# LightTester/LightTest.py 

import sys 
sys.path.append(".")

from pprint import pprint 

class LightTest:
    ''' LightTest class '''
    
    lights = None
    
    
    # class constructor creates instance of LightTest, input N to create 2d list
    def __init__(self, N):
        self.size = N
        self.lights = [[0]*N for _ in range(N)]
        
         
    # method to apply instructions to 2d list
    def apply(self, instructions):
        for line in instructions:
            cmd, x1, y1, x2, y2 = line
            print('L: {}'.format(line))
            if line != None:
                x1, y1, x2, y2 = self.coordCheck(x1, y1, x2, y2)# new line
                if cmd == "turn on":
                    #line.coordCheck()
                    for i in range(x1, x2+1):
                       for j in range(y1, y2+1):
                           self.lights[i][j] = 1
                elif cmd == "turn off":
                    #line.coordCheck()
                    for i in range(x1, x2+1):
                        for j in range(y1, y2+1):
                            self.lights[i][j] = 0
                elif cmd == "switch":
                    #line.coordCheck()
                    for i in range(x1, x2+1):
                        for j in range(x1, x2+1):
                            if self.lights[i][j] == 0:
                                self.lights[i][j] = 1
                            elif self.lights[i][j] == 1:
                                self.lights[i][j] = 0
                                
                    
    def coordCheck(self, x1, y1, x2, y2):
        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if x2 > self.size:
            x2 = self.size
        if y2 > self.size:
            y2 = self.size 
        return x1, y1, x2, y2
        
        
    def count(self):
        ''' method to count the number of lights on (off = 0, on = 1) '''
        lightcount = 0
        rowCount = len(self.lights)
        columnCount = len(self.lights[0])
        
        for r in range(0, rowCount):
            for c in range(0, columnCount):
                if self.lights[r][c] == 1:
                    lightcount+=1
                    
        return lightcount 
    


