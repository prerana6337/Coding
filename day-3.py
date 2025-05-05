#private method usage
class abc():
  def __init__(self,var):
    self.__var=var
  def __display(self): #underscore is taken for private method
    print("from class method,var=", self.__var)
obj=abc(10)
obj.__abc__display()

Output:
from class method,var= 100
-----------------------------------------------
#calling a method from another method in the same class
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is:",self.var)
    def add_value(self):
        self.var+=5
        self.display()
obj=abc(10)
obj.add_value()

Output:
Var is: 15
------------------------------------------------
#class method,which calls a functon defined global namespace
def xxx(x):
    return x*10
class xyz():
    def __init__(self ,var):
        self.var=var
    def display(self):
        print("Var is:",self.var)
    def modify(self):
        self.var=xxx(self.var)
obj=xyz(10)
obj.display()
obj.modify()
obj.display()

Output:
Var is: 10
Var is: 100
-------------------------------------------------
'''built_in methods- get,set,delete
getattr(),setattr(),deleteattr()'''
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is:",self.var)
obj=abc(10)
obj.display()
print("obj has attribute var:", hasattr(obj,'var'))
getattr(obj,'var')
setattr(obj,'var',20)
print("Ater setting value:",obj.var)
setattr(obj,'count',10)
print("new var count is created wt value:",obj.count)
delattr(obj,'var')
print("after deleteing",obj.var)

Output:
Var is: 10
obj has attribute var: True
Ater setting value: 20
new var count is created wt value: 10
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
Cell In[21], line 17
     15 print("new var count is created wt value:",obj.count)
     16 delattr(obj,'var')
---> 17 print("after deleteing",obj.var)

AttributeError: 'abc' object has no attribute 'var'
---------------------------------------------------------------------------
'''built-in functions for class attributes
1. .__doc__ : when string doc is not specified no return attr
2. .__dict__ : namespace accessed attribtues
3. .__name__ :return class attr's name
4. .__module__ :retrn module
5. .__bases__ : inheritance
'''
# '.'--permission accessor

class abc():
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2
    def display(self):
        print("var1:",self.v1)
        print("var2:",self.v2)
obj=abc(10,12.345)
obj.display()
print("Object.__dict__ :",obj.__dict__)
print("Object.__doc__ :",obj.__doc__)
print("Class.__name__ :",abc.__name__)
print("Object.__module__ :",obj.__module__)
print("Class.__bases__ :",abc.__bases__)

Output:
var1: 10
var2: 12.345
Object.__dict__ : {'v1': 10, 'v2': 12.345}
Object.__doc__ : None
Class.__name__ : abc
Object.__module__ : __main__
Class.__bases__ : (<class 'object'>,)
----------------------------------------------------------------
'''prog that uses class as student to store the name and marks of the student, use list to store the marks of 3 subjects.
Constraints:
1. Take class as student
2. Create a constructor for the student name
3.Create a function for marks, to be entered manually within the class function and add the marks to the list.
4.display the student name and marks he/she got.
TC:
obj1: "vijay"
obj2:"Anil"
Output:
Vijay got [88,90]
Anil got [91,93]'''

class student():
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def entmarks(self):
        for i in range(0,3):
            n=int(input("Enter %s marks in %d subject: "%(self.name,i+1)))
            self.marks.append(n)
    def display(self):
        print(self.name,"got",self.marks)
a=student("Vijay")
a.entmarks()
b=student("Anil")
b.entmarks()
a.display()
b.display()

Output:
Enter Vijay marks in 1 subject:  99
Enter Vijay marks in 2 subject:  98
Enter Vijay marks in 3 subject:  89
Enter Anil marks in 1 subject:  45
Enter Anil marks in 2 subject:  78
Enter Anil marks in 3 subject:  67
Vijay got [99, 98, 89]
Anil got [45, 78, 67]
-------------------------------------------------------------------
'''program that has a class circle ,use a class variable to define value of constant pi. Use this class variable to calculate the area and circumference of circle with specified radius
Constraints:
pi with the class variable as 3.14159
radius=7.5
return the area and circumference values to maintain prog by creating function within the class respectively.
'''
class var():
    pi=3.14159
    def __init__(self,rad):
        self.rad=rad
    def area():
        return pi*rad*rad
    def cir():
        return 2*pi*rad
    def display(self):
        print("Area:",self.area())
        print("Cicumference:",self.cir())
obj=var(7.5)
obj.display()
        
    
