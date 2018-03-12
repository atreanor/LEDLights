

class LightTest:
    ''' LightTest class '''
    
    lights = None
    
    # class constructor creates instance of LightTest, input N to create 2d list
    def __init__(self, N):
        self.lights = [[0]*N for _ in range(N)]
        self.size = N
    # method to apply instructions to 2d list
    def apply(self, instructions):
        for line in instructions:
            print(line)
            if line != None:
                cmd = line[1]        
                x1,y1,x2,y2 = int(line[2]),int(line[3]),int(line[4]),int(line[5])
                print(cmd, x1, y1, x2, y2)
                # check boundaries of coordinates
                if x1 < 0 or y1 < 0 or x2 > self.size or y2 > self.size:
                    x1, y1, x2, y2 = coordCheck(x1, y1, x2, y2)
                
                if cmd == "turn on":
                    self.lights[x1:x2+1, y1:y2+1] = 1
                elif cmd == "turn off":
                    self.lights[x1:x2+1, y1:y2+1] = 0
                elif cmd == "switch":
                    for i in self.lights[x1:x2+1, y1:y2+1]:
                        if i == 1:
                            i = 0
                        elif i == 0:
                            i = 1  
        
                    
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
    