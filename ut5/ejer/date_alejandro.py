from __future__ import annotations
INITIAL_YEAR, FINAL_YEAR = 1900, 2050
MONTHS_NAMES = {
    1: "january",
    2: "february",
    3: "march",
    4: "april",
    5: "may",
    6: "june",
    7: "july",
    8: "august",
    9: "september",
    10: "october",
    11: "november",
    12: "december"
}
WEEKDAYS_NAMES = {
    0: "sunday",
    1: "monday",
    2: "tuesday",
    3: "wednesday",
    4: "thursday",
    5: "friday",
    6: "saturday"
}
class Date:
    def __init__(self, day: int, month: int, year: int):
        """validate day-month-year (from 1-1-1990 to 31-12-2050) and leap years
        incorrect day: day = 1, incorrect month: month = 1, incorrect year: year = 1900"""
        self.year = year if INITIAL_YEAR <= year <= FINAL_YEAR else INITIAL_YEAR
        self.month = month if 1 <= month <= 12 else 1
        self.day = day if 1 <= day <= self.days_in_month() else 1
    
    @staticmethod
    def static_is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    @staticmethod
    def static_days_in_month(month: int, year: int) -> int:
        if month == 2:
            return 29 if Date.static_is_leap_year(year) else 28
        return 30 if month in [4,6,9,11] else 31

    def is_leap_year(self) -> bool:
        return Date.static_is_leap_year(self.year)
    
    def days_in_month(self) -> int:
        return Date.static_days_in_month(self.month, self.year)

    def qty_of_leap_years(self) -> int:
        return (self.year - INITIAL_YEAR) // 4
    
    def days_elapsed_in_the_year(self) -> int:
        """days elapsed from the beginning of the self.year to the self.day"""
        return sum(Date.static_days_in_month(i, self.year) for i in range(1, self.month)) + self.day
        
    def delta_days(self) -> int:
        """days elapsed from 1-1-1900 to the marked date"""
        days_in_previous_years = (self.year - INITIAL_YEAR) * 365 + self.qty_of_leap_years()
        return days_in_previous_years + self.days_elapsed_in_the_year() - 1

    def weekday(self) -> int:
        weekday = self.delta_days() % 7 + 1
        return weekday if weekday != 0 else 7

    def is_weekend(self) -> bool:
        return self.weekday() in [0, 6]

    def short_date(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __str__(self) -> str:
        return f"{WEEKDAYS_NAMES[self.weekday()]} {self.day} {MONTHS_NAMES[self.month]} {self.year}"
    
    def __add__(self, days_to_add) -> object:
        """addition operator, to add days to the marked date"""
        new_day = self.day + days_to_add
        new_month, new_year = self.month, self.year
        while new_day > Date.static_days_in_month(new_month, new_year):
            new_day -= Date.static_days_in_month(new_month, new_year)
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1
        return Date(new_day, new_month, new_year)

    def __sub__(self, other):
        """subtraction operator, to subtract days or a date from the marked date"""
        if isinstance(other, int):
            new_day = self.day - other
            new_month, new_year = self.month, self.year
            while new_day < 0:
                new_day += Date.static_days_in_month(new_month, new_year)
                new_month -= 1
                if new_month > 12:
                    new_month = 1
                    new_year += 1
            return Date(new_day, new_month, new_year)
        if isinstance(other, Date):
            return abs(self.delta_days() - other.delta_days())

    def __eq__(self, other) -> bool:
        return self.delta_days() == other.delta_days()
    
    def __lt__(self, other) -> bool:
        return self.delta_days() < other.delta_days()
    
    def __gt__(self, other) -> bool:
        return self.delta_days() > other.delta_days()    

date1 = Date(18, 4, 2023)
date2 = Date(11, 4, 2023)
date3 = Date(11, 4, 2023)
date4 = Date(9, 5, 1992)
print(f"✓ Is leap year: {date1.is_leap_year()}")
print(f"✓ Amount of the leap years is: {date1.qty_of_leap_years()}")
print(f"✓ Days elapsed in the year is: {date1.days_elapsed_in_the_year()}")
print(f"✓ Days in month is: {date1.days_in_month()}")
print(f"✓ The short date is: {date1.short_date()}")
print(f"✓ Days elapsed from 01/01/1900 is: {date1.delta_days()}")
print(f"✓ The weekday's number is: {date1.weekday()}")
print(f"✓ Is weekend: {date1.is_weekend()}")
print(f"✓ The STR format is: {date1}")
print(f"✓ Is {date2.short_date()} equal to {date3.short_date()}: {date2 == date3}")
print(f"✓ Is {date2.short_date()} greater than {date4.short_date()}: {date2 > date4}")
print(f"✓ Is {date2.short_date()} lower than {date4.short_date()}: {date2 < date4}")
print("✓ Calculation of additions and subtractions:")
print(f"  - Result of the addition: {date1 + 10}")
print(f"  - Result of the subtraction: {date1 - 24}")
print(f"  - Result of the subtraction: {date1 - date4}")
print(date4)