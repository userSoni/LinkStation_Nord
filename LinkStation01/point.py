import math

class Point:
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
    def __add__(self, other):
        
        # print("Point value of x = %d and y = %d" % (self.x, self.y))
        return (math.sqrt(((self.x - other.x)**2) + ((self.y - other.y)**2)))