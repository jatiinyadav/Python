
#keyworded variable length argument

def person(**data):     
    # print(name)
    for i,j in data.items():
        print(i,j)

person( Name =  ' =  JATIN', Age =' =  19', Mob = ' =  998273', City = ' =  Delhi')
print("------") 
