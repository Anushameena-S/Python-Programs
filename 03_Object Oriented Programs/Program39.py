#Multiple Constructors - Destructors

class Date(object):
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    @classmethod
    def dmy(cls,day,month,year):
        cls.year=year
        cls.month=month
        cls.day=day
        return cls(cls.year,cls.month,cls.day)

    @classmethod
    def mdy(cls,month,day,year):
        cls.year=year
        cls.month=month
        cls.day=day
        return cls(cls.year,cls.month,cls.day)

a=Date(2000,7,8)
print(a.year)
b=Date.dmy(9,7,2012)
print(b.year)
c=Date.mdy(4,5,2014)
print(c.year)


    
