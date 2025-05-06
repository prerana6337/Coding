'''-----OOPS----------
-MULTILEVEL
-MULTIPLE
-HIERARCHY
-HYBRID'''
#multiple inheritance
class base1(object): #1st base class
    def __init__(self):
        super(base1,self).__init__()
        print("Base class-1")
class base2(object): #2nd base class
    def __init__(self):
        super(base2,self).__init__()
        print("Base class-2")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("Derived class from both clases.")
d=derived()

Output:
Base class-2
Base class-1
Derived class from both clases
--------------------------------------------------
'''intialize classes addition,multiplication in a calculator. pass the values from main program to the super class where the sub classes addition 
and multiplication were triggered and return the outputs respectively.
1.take derived class calc
2.from derived class call sub classes add and mul
3.return the values after math to the object
4.maual values of both numbers considered within the object '''
class add():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def ad(self):
        return self.a+self.b
class mul():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def mu(self):
        return self.a*self.b
class calci(add,mul):
    def __init__(self,a,b):
        add.__init__(self,a,b)
        mul.__init__(self,a,b)
        print("Calci class initialized")
x=int(input("Enter a:"))
y=int(input("Enter b:"))
c=calci(x,y)
print("sum:",c.ad())
print("mul:",c.mu())
    
Output:
Enter a: 2
Enter b: 3
Calci class initialized
sum: 5
mul: 6
---------------------------------------------------------------
#multilevel inheritance
class person:
    def name(self):
        print("name:")
class teacher(person):
    def qualification(self):
        print("PHD")
class hod(teacher):
    def exp(self):
        print("experience...15 yrs")
head=hod()
head.name()
head.qualification()
head.exp()

Output:
name:
PHD
experience...15 yrs
------------------------------------------------------------------
class sqr():
    def __init__(self,a):
        self.a=a
    def sq(self):
        return self.a*self.a
class cub():
    def __init__(self,a):
        self.a=a
    def cu(self):
        return self.a*self.a*self.a
class sum(sqr,cub):
    def __init__(self,a):
        sqr.__init__(self,a)
        cub.__init__(self,a)
x=int(input("Enter a:"))
c=sum(x)
print("sqr:",c.sq())
print("cub:",c.cu())
print(c.sq()+c.cu())

Output:
Enter a: 2
sqr: 4
cub: 8
12
--------------------------------------------------------------------
#multi levl inheritance cubes and squares of an obj
class num():
    def __init__(self,a):
        self.a=a
class sq(num):
    def sqr(self):
        return self.a**2
class cu(sq):
    def cub(self):
         return self.a**3
a=int(input("enter:"))
c=cu(a)
print(c.sqr())
print(c.cub())

enter: 2
4
8
----------------------------------------------------------------------
#------------multipath-------
#-----------exceptional handling,error handling,file handling-------------
#hierarchy inheritance
class num():
    def __init__(self,n):
        self.n=n
    def get_num(self):
        return self.n
class double(num):
    def result(self):
        return self.get_num() *2
class triple(num):
    def result(self):
        return self.get_num() *3
d=double(2)
print("double:",d.result())
t=triple(3)
print("Triple:",t.result())

Output:
double: 4
Triple: 9
------------------------------------------------------------------------
 #composition or containership----used for complex objects-----
#abstract class
class fruit:
    def taste(self):
        raise NotImplementedError()
    def vitamin(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()   
class mango(fruit):
    def taste(self):
        return "sweet"
    def vitamin(self):
        return "a"
    def color(self):
        return "yellow" 
class orange(fruit):
    def taste(self):
        return "sour n sweet"
    def vitamin(self):
        return "c"
    def color(self):
        return "orange" 
Alphanso=mango()
print(Alphanso.taste(),Alphanso.vitamin(),Alphanso.color())
org=orange()
print(org.taste(),org.vitamin(),org.color())

Output:
sweet a yellow
sour n sweet c orange
--------------------------------------------------------------

