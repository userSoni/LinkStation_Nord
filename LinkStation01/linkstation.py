from point import Point

class LinkStation(Point):
    
    def __init__(self, x, y, reach):
        
        super().__init__(x, y)
        self.reach = reach
  
    def get_power(self, other):
        
        distance = super().__add__(other)
        
        if distance > self.reach:
            return(self.reach - distance)**2 
        else:
            return 0