#class declaration

class abc():
    var=100
    def display(self):
        print("message")
obj=abc()
print(obj.var)
obj.display()

Output:
100
message
---------------------------------
#class constructor __init__(method)

class abc():
    def __init__(self,val):
        print("message")
        self.val=val
        print("value:",val)
obj=abc(100)

Output:
message
value: 100
---------------------------------
#class object variables

class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("obj var:",var)
        print("class var:",abc.cv)
obj=abc(10)
obj=abc(20)

Output:
obj var: 10
class var: 1
obj var: 20
class var: 2
----------------------------------
CLASS TRIGGERING INVOKING

----------------------------------
#Code to ilustrate the modification of an instance 
class num():
    even=0
    def check(self,val):
        return val%2==0
    def evod(self,val):
        if self.check(val):
            print("even")
        else:
            print("odd")
n=num()
n.evod(12)
n.evod(13)

Output:
even
odd
------------------------------------
'''segregate the even and odd parameters in a list and print even list and odd list separately using a class "number"
n1=num(21)
n2=num(32)
n3=num(43)
n4=num(54)
n5=num(65)
op:
even:[32,54]
odd:[21,43,65]'''

class number():
    even=[]
    odd=[]
    def __init__(self,var):
        self.var=var
        if var%2==0:
            number.even.append(var)
        else:
            number.odd.append(var)
n1=number(21)
n1=number(32)
n1=number(43)
n1=number(54)
n1=number(65)
print(number.even)
print(number.odd)    

Output:
[32, 54]
[21, 43, 65]
-------------------------------------
#delete method- __del__()

class abc():
    cv=0
    def __init__(self,var):
        abc.cv+=1
        self.var=var
        print("obj var:",var)
        print("class var:",abc.cv)
    def __del__(self):
        abc.cv-=1
        print("object with %d is going out of scope"%self.var)
obj1=abc(10)
obj2=abc(20)
del obj1
del obj2

Output:
obj var: 10
class var: 1
obj var: 20
class var: 2
object with 10 is going out of scope
object with 20 is going out of scope
---------------------------------------

CLASS MEMBERS-USING CLASS+OBJECT
__repr__ : return string representation
__cmp__ : compare two classes
__len__ : length of the class object
----------------------------------------
CODE:
class abc():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __cmp__(self,obj):
        return self.var-obj.var
    def __len__(self):
        return len(self.name)
obj=abc("prerana",10)
print("the value stored in object is:",repr(obj))
print("the length of name name stored in object:",len(obj))
obj1=abc("sindhu",1)
val=obj.__cmp__(obj1)
if val==0:
    print("equal")
elif val==-1:
    print(" 1st val less than 2nd val.")
else:
    print("1st val greates than 2 nd val.")

Output:
the value stored in object is: 10
the length of name name stored in object: 7
1st val greates than 2 nd val.

  

