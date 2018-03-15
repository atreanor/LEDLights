# LightTester/LightTest.py 
import sys 
sys.path.append(".")

from pprint import pprint 

class LightTest:
    ''' LightTest class '''
    
    lights = None
    
    
    # class constructor creates instance of LightTest, input N to create 2d list
    def __init__(self, N):
        ''' class constructor '''
        self.size = N
        self.lights = [[0]*N for _ in range(N)]
        
         
    # method to apply instructions to 2d list
    def apply(self, N, instructions):
        ''' method to apply instructions to grid, 0 = off, 1 = on '''
        
        for line in instructions:
            cmd, x1, y1, x2, y2 = line
            # print('L: {}'.format(line))
            if line != None:
                if x1 < 0:
                    x1 = 0
                if y1 < 0:
                    y1 = 0
                if x2 > N:
                    x2 = N-1
                if y2 > N:
                    y2 = N-1
                    
                if cmd == "turn on":                    
                    for i in range(x1, x2+1):
                       for j in range(y1, y2+1):
                           self.lights[i][j] = 1
                           
                elif cmd == "turn off":                    
                    for i in range(x1, x2+1):
                        for j in range(y1, y2+1):
                            self.lights[i][j] = 0
                elif cmd == "switch":
                    
                    for i in range(x1, x2+1):
                        for j in range(x1, x2+1):
                            if self.lights[i][j] == 0:
                                self.lights[i][j] = 1
                            elif self.lights[i][j] == 1:
                                self.lights[i][j] = 0
       
        
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
    
    


