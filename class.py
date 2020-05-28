#This program is for the Operator overriding



#This is for the add method

class Operator:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.result=None

    def __add__(self,oth):
        print('The number of time call')
        self.res1=self.a+oth.a
        self.res2=self.b+oth.b
        self.res3=self.c+oth.c
        return Operator(self.res1,self.res2,self.res3)

    def __str__(self):
        return 'The result of {} and {} and {} after perform operation is:{}'.format(self.a,self.b,self.c,self.result)

    

#Creating the objects of the class
op=Operator(10,11,21)
op1=Operator(32,12,12)
op2=Operator(342,13,10)
x=op+op1+op2
print(x.a)
print(x.b)
print(x.c)
print(op.__str__())
print(op.__dict__)
print(op1.__str__())
print(op1.__dict__)
print(op2.__str__())
print(op2.__dict__)
        
            
