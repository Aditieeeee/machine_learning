class Fraction:
    num=None
    den=None

    def __init__(self,x,y):
        self.num=int(x)
        self.den=int(y)

    def show(self):
        print(self.num,"/",self.den)
    #   this gives space betweeeen print

    def __str__(self):
        return "{0}/{1}".format(self.num,self.den)
    # but this is a magic method which , __str__ , which gives the output which is written in this method . bhale ans kuch bhi ho , agar object print karwanege jo isme liha hoga wahi print hoga by rrint(var)


    def __add__(self,other):
        tempN=self.num*other.den +other.num*self.den
        tempD=self.den * other.den

        return Fraction(tempN,tempD)

    # this def __add__ magic method is : used to add the given objects .
    # self stores a(3,4)
    # other stores b(3,7)

    def __sub__(self,other):
            tempN=self.num*other.den -other.num*self.den
            tempD=self.den * other.den
    
            return Fraction(tempN,tempD)

    def __mul__(self,other):
             tempN=self.num * other.num
             tempD=self.den * other.den
     
             return Fraction(tempN,tempD)


    def __truediv__(self,other):
             tempN=self.num*other.den 
             tempD=self.den * other.num
             
             return Fraction(tempN,tempD)


    def simply(self):
          l1=[]
          l2=[]
          for i in range(1,self.num+1):
                if(self.num%i==0):
                      l1.append(i)

          for i in range(1,self.den+1):
                if(self.den%i==0):
                      l2.append(i)


    #   APPROACH 1 , BY USING POP()
        #   for i in range(len(l1)+1):
        #         m=max(l1)
        #         if m in l2:
        #               break
        #         else:
        #               l1.pop()

        #  APPROACH 2ND BY UPADATING M by the largest number 
          m = 1

          for i in l1:
           if i in l2:
            m = i
     
          return Fraction((self.num)//m,(self.den)//m)          
                                            #  use the floordivision to avoid the decimal point value .
                   