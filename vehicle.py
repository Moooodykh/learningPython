# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:47:19 2019

@author: mkharbou
"""

class Vehicl:
    def __init__(self):
        print("Initializing..")
        self.vehicleType ='Undefined'
        self.weight = 0
        
    def setType(self, newType):
        self.vehicleType = newType
    
    def setWeight(self, weight):
        self.weight = weight
    
    def getInfo(self):
        print('Vehicle')
        print('|-->type : %s' % self.vehicleType)
        print('|-->weight : %s' % self.weight)
        

If __name__ == "__main__":
    v = Vehicle()
    v.getInfo()