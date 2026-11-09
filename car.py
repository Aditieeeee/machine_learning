class Car:

    def getinfo(self,x,y):
        self.color=x
        self.topSpeed=y

        print("the car has color",self.color,"and top speed of",self.topSpeed)

    def calAvgSpeed(self,km,t):
        speed=km/t
        print("avg speed is", speed)    


