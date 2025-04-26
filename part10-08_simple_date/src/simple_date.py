class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"
    
    def __lt__(self, another_date):
        if self.__year != another_date.__year:
            return self.__year < another_date.__year
        elif self.__month != another_date.__month:
            return self.__month < another_date.__month
        else :
            return self.__day < another_date.__day
        
    def __gt__(self, another_date):
        if self.__year != another_date.__year:
            return self.__year > another_date.__year
        elif self.__month != another_date.__month:
            return self.__month > another_date.__month
        else :
            return self.__day > another_date.__day      
        
    def __eq__(self, another_date):
        return self.__year == another_date.__year and self.__month == another_date.__month and self.__day == another_date.__day
    
    def __ne__(self, another_date):
        return self.__year != another_date.__year or self.__month != another_date.__month or self.__day != another_date.__day

    def __month_to_days(self):
        return self.__month * 30 + self.__day
    
    def __years_to_days(self):
        return self.__day + self.__month * 30 + self.__year * 360
    
    def __set_date(self, days : int):
        self.__month = days // 30
        self.__day = days - self.__month * 30

        while self.__day > 30 :
            self.__month += 1
            self.__day -= 30
        while self.__month > 12 :
            self.__year += 1
            self.__month -= 12


    def __add__(self, days : int):
        new_date = SimpleDate(0,0,self.__year)
        new_date.__set_date(self.__month_to_days() + days)
        return new_date
    
    def __sub__(self, another_date):
        diff = abs(self.__years_to_days() - another_date.__years_to_days())
        return diff

if __name__ == "__main__":

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
