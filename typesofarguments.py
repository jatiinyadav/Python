def add(a,b):          # a and b are actual arguments 1.Position 2. Keyword 3. default 4. Variable LENgth
    c = a + b
    print(c)

add(4,7)
print("------")

def person(age,name):
    print(age + 1)
    print(name)             #position

person(19,'JAtin')
print("------")

def person(age,name):
    print(age - 1)
    print(name)

person(name = 'Jatin', age = 20)        #keyword
print("------")

def person(age = 18):
    print(age)

person()                #default
print("------")

def sum(a, *b):     #length variable
    a = 0
    for i in b:
        a  = a + i 
    print(a)

sum (12,34,45,90)
print("------")

#keyworded variable length argument

def person(name, **data):       # function ke andar hum use value assign kar sakte
    print(name)
    for i,j in data.items():
        print(i,j)

person('JATIN', age ='19', mob = '998273', city = 'Delhi')      #jaise yaha pe assign kiya hai
print("------") 


#global keyword 

#preference will be give 1st to local variable

a = 10
print(id(a))
def maggi(): 
    a = 9
    x = globals()['a']
    print(x)
    print(id(x))
    print("In fun", a)
    globals()['a'] = 15
    
maggi()
print("Outside",a)
print("------")