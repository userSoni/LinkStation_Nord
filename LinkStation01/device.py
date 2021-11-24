from point import Point

class Device(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
                     
    def get_ispower(self, link_station):
        
        get_station = link_station[0]
        best_power = 0
        
        for station in link_station:
            power = station.get_power(self)
            
            if power > best_power:
                get_station = station
                best_power = power
                return ("Best link station for point %d %d is %d, %d with power %d.") % (self.x, self.y, get_station.x, get_station.y, best_power)
            
            else:
                return "No link station within reach for point %d, %d." % (self.x, self.y)