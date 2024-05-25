def dontshow(value):
    print(value)
dontshow("hello friends") 
#len() function returns the length (number of item)of an object
length=len("hello world!")
print(length)
#  range() function generates a sequence of numbers within specifier
#commonly used in loops 
#for (int i=0;i<10;i++)
#for(number in range starting from 0 )
for num in range(5):
    print (num)
for value in range(1,20,3):
    print(value)
#list in python 
my_list=[1,2,4,6,'a','b','c']
length=len(my_list)
print(my_list[3])
print(my_list[1])
#this.name=name
class car:
    def __init__(self,make,model):#init is constructor
        self.make=make
        self.model=model
    #this is method
    def show_info(self):
      print("car:"+self.make+" "+self.model)
car1=car("toyata","corolla")
car2=car("hyundai","zen")
print(car1.make+" "+ car2.model)
car1.show_info()

    #@classmethod,@staticmethod{difference identity}

#create folder"templates" inside categories folder
#create folder"categories"inside template folder
#create file"categories_list.html and categories_products.html"inside categories
#get and post
#get-urls query param
#post-body params
