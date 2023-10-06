class Time:
    """Blueprint for Time object"""
    #__init__ : Python keyword for class constructor
    #applies to all class constructors
    #self.: class instance object, obj. ref arg., obj. ref.
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0
    
    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def print_time(self):
        print (self.__hour, ":", self.__minute, ":", self.__second)

    def set_second(self, second):
        if(second >= 0 and second <= 59):
            self.__second = second
        else:
            self.__second = 0

    def get_second(self):
        return self.__second

    def set_hour(self, hour):
        if(hour >= 0 and hour <= 23):
            self.__hour = hour
        else:
            self.__hour = 0

    def get_hour(self):
        return self.__hour

    def set_minute(self, minute):
        if (minute >= 0 and minute <= 59):
            self.__minute = minute
        else:
            self.__minute = 0

    def get_minute(self):
        return self.__minute

    def tick(self):
        self.__second = __second +1
        if(self.__second == 60):
            self.__second = 0
            self.__minute = self.__minute + 1
            if(self.__minute == 60):
                self.__minute = 0
                self.__hour = self.hour + 1
                if(self.__hour == 24):
                    self.__hour = 0
