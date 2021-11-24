#import numpy as py
from linkstation import LinkStation
from device import Device

def run_default_data():
    link_st = [
        LinkStation(0, 0, 10),
        LinkStation(20, 20, 5),
        LinkStation(10, 0, 12)
    ]
    
    device = [
        Device(0, 0),
        Device(100, 100),
        Device(15, 10),
        Device(18, 18)
    ]
    
    results = ""
    
    for devi in (device):
        results += devi.ispower(link_st)
        # results = results + devi.ispower(link_st)
        #print(results)
    return results.split(".")

def check_data():

    print(run_default_data())

if __name__ == '__main__':
    check_data()