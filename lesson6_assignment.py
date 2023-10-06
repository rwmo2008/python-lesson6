from lesson6 import Time

myTime = Time()
myTime.set_time(1, 2, 3)
print(myTime.get_hour)
print(myTime.get_minute)
print(myTime.get_second)


for i in range(20):
    myTime.print_time()
    myTime.tick()
