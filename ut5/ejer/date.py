START_YEAR, FINAL_YEAR = 1900, 2050
MONTHS = {
    1: ("january", 31),
    2: ("february", 28),
    3: ("march", 31),
    4: ("april", 30),
    5: ("may", 31),
    6: ("june", 30),
    7: ("july", 31),
    8: ("august", 31),
    9: ("september", 30),
    10: ("october", 31),
    11: ("november", 30),
    12: ("december", 31),
}
WEEKDAYS = {
    0: "sunday",
    1: "monday",
    2: "tuesday",
    3: "wednesday",
    4: "thursday",
    5: "friday",
    6: "saturday",
}
class Date:
    def __init__(self, day: int, month: int, year: int):
        """validate day-month-year (from 1-1-1990 to 31-12-2050) and leap years
        incorrect day: day = 1, incorrect month: month = 1, incorrect year: year = 1900"""
        self.year = year if START_YEAR <= year <= FINAL_YEAR else START_YEAR
        self.month = month if 1 <= month <= 12 else 1
        self.day = day if 1 <= day <= self.days_in_month() else 1

    def is_leap_year(self) -> bool:
        return (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0
    
    def days_in_month(self) -> int:
        if self.month == 2 and self.is_leap_year():
            return MONTHS[self.month][1] + 1
        return MONTHS[self.month][1]

    @staticmethod
    def static_days_in_month(month: int, year: int) -> int:
        is_leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
        if month == 2 and is_leap_year:
            return MONTHS[month][1] + 1
        return MONTHS[month][1]

    def qty_of_leap_years(self) -> int:
        return (self.year - START_YEAR) // 4
    
    def days_elapsed_in_the_year(self) -> int:
        """days elapsed from the beginning of the year of the date to the exact date"""
        return sum(MONTHS[i][1] for i in range(1, self.month)) + self.day
    
    def delta_days(self) -> int:
        """days elapsed from 1-1-1900 to the marked date"""
        days_in_previous_years = (self.year - START_YEAR) * 365 + self.qty_of_leap_years()
        return days_in_previous_years + self.days_elapsed_in_the_year() - 1

    def weekday(self) -> int:
        weekday = (self.delta_days() + 1) % 7
        return weekday if weekday != 7 else 0

    def is_weekend(self) -> bool:
        return self.weekday() in [0, 6]

    def short_date(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __str__(self) -> str:
        return f"{WEEKDAYS[self.weekday()]} {self.day} {MONTHS[self.month][0]} {self.year}"
    
    def __add__(self, days_to_add) -> object:
        """addition operator, to add days to the marked date"""
        new_day, new_month, new_year = (self.day + days_to_add), self.month, self.year
        while new_day > Date.static_days_in_month(new_month, new_year):
            new_day -= Date.static_days_in_month(new_month, new_year)
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1
        return Date(new_day, new_month, new_year)

    def __sub__(self, other) -> object:
        """subtraction operator, to subtract days or a date from the marked date"""
        if isinstance(other, int):
            new_day = abs(self.day - other)
            new_month = self.month
            new_year = self.year
            while new_day > MONTHS[new_month][1]:
                new_month -= 1
                new_new_day = MONTHS[new_month][1] - new_day
                if new_month == 0:
                    new_month = 12
                    new_year -= 1
            return Date(new_day, new_month, new_year)
        if isinstance(other, Date):
            pass

    def __eq__(self, other) -> bool:
        return self.delta_days() == other.delta_days()
    
    def __lt__(self, other) -> bool:
        return self.delta_days() < other.delta_days()
    
    def __gt__(self, other) -> bool:
        return self.delta_days() > other.delta_days()    

date1 = Date(20, 2, 1992)
date2 = Date(11, 4, 2023)
date3 = Date(11, 4, 2023)
print(date1.is_leap_year())
print(date1.qty_of_leap_years())
print(date1.days_elapsed_in_the_year())
print(date1.days_in_month())
print(date1.short_date())
print(date1.delta_days())
print(date1.weekday())
print(date1.is_weekend())
print(date1)
date5 = (date1 + 60)
print(date5)
# print(date1 - 24)
# print(date2 == date3)
# print(date2 > date3)
# print(date2 < date3)