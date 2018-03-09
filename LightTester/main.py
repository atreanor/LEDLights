import sys

def main(input=None):
    '''main method'''
    print("input", input)
    
    # parse input with regex, output N & instructions
    N, instructions = parseFile(input)
    
    #create 2d list of N dimensions
    ledTester = LightTester(N)
    pprint(lights)
    
    #read instructions and invoke apply
    for cmd in instructions:
        ledTester.apply(instruction)
    
    
    
    #count and print lights on   
    print("Lights on: ", lights.count())
    return 0
if __name__ == "__main__":
    sys.exit(main()) # pragma: no cover 

