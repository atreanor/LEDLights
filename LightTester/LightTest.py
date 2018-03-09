class LightTester:
    ''' LightTester class '''
    lights = None
    
    # creates instance of class, input N from parser to create 2d list
    def __init__(self, N):
        self.lights = [[0]*N for _ in range(N)]
        self.N = N
        
    def apply(self, cmd):
        
        if cmd is 'turn on':
            #action
            pass
        elif cmd is 'turn off':
            #action
            pass
        elif cmd is 'switch':
            #action
            pass
    
    def count(self):
        ''' method to count the number of lights on 1 '''
        lightcount = 0
        rowCount = len(self.lights)
        columnCount = len(self.lights[0])
        
        for r in range(0, rowCount):
            for c in range(0, columnCount):
                if self.lights[r][c] == 1:
                    lightcount+=1
                    
        return lightcount 
    
    
    def input(self, fname):
        fname = input('Enter filename: ')
        if fname == "":
            print('Error: please enter filename')
        elif fname
        
    '''
    """ The LEDLightsTester class creates an instance with a 2 
    dimensional list of input size"""
    lightList = None 
    
    def __init__(self, size):
        # create class instance, and 2d list
        self.lightList = [[0]*size for _ in range(size)]
    
    def apply(self, cmd):
        if cmd is 'turn on':
            
        elif cmd is 'turn off':
            #instructions
        elif cmd is 'switch':
            #instructions
    def count(self):
        return count '''

    
    