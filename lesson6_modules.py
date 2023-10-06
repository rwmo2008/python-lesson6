#from <file> import <class>
from lesson6 import Time

#Time objects    
myTime1 = Time()
myTime1.set_time(1, 2, 3)
myTime2 = Time()
myTime2.set_time(12, 0, 0)

myTime1.print_time()
myTime2.print_time()

myTime1.hour = 50
myTime1.print_time()

#invalid
#print (myTime1.__second)

#outputs documentation string from class file
print("Using object name:")
print(myTime1.__doc__)

print()

#documentation string using class name instead of object name
print("Using class name:")
print(Time.__doc__)

#<class '__main__.Time'>
print(myTime1.__class__)


