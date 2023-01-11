class Time:
    def __init__(self):
        self.__h=int(input("Enter the time in hours:"))
        self.__m=int(input("Enter the time in minutes:"))
        self.__s=int(input("Enter the time in seconds:"))
    def __add__(self,tobj2):
        hours=self.__h + tobj2.__h
        print("Sum of hours",hours)
        minutes=self.__m + tobj2.__m
        print("Sum of minutes",minutes)
        seconds=self.__s + tobj2.__s
        print("Sum of seconds",seconds)
        try:
           while minutes >= 60:
                 hours=hours+1
                 minutes=minutes-60
           while seconds >= 60:
                 minutes=minutes+1
                 seconds=seconds-60
        except:
               print("can't be displayed")
        return hours,minutes,seconds
print("Enter the time of 1st object:")
tobj1=Time()
print("Enter the time of 2nd object:")
tobj2=Time()
print("Sum of two time is: (Hour,Minutes,Seconds)",tobj1+tobj2)