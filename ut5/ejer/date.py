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
        self.day = day if 1 <= day <= Date.static_days_in_month(self.month, self.year) else 1
    
    @staticmethod
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def qty_of_leap_years(self) -> int:
        return (self.year - INITIAL_YEAR) // 4

    def days_elapsed_in_the_year(self) -> int:
        """days elapsed from the beginning of the self.year to the self.day"""
        return sum(Date.static_days_in_month(i, self.year) for i in range(1, self.month)) + self.day
        
    def get_delta_days(self) -> int:
        """days elapsed from 1-1-1900 to the marked date"""
        days_in_previous_years = (self.year - INITIAL_YEAR) * 365 + self.qty_of_leap_years()
        return days_in_previous_years + self.days_elapsed_in_the_year() - 1
    
    @staticmethod
    def static_days_in_month(month: int, year: int) -> int:
        if month == 2:
            return 29 if Date.is_leap_year(year) else 28
        return 30 if month in [4,6,9,11] else 31

    @property
    def days_in_month(self) -> int:
        return Date.static_days_in_month(self.month, self.year)

    
    @property
    def weekday(self) -> int:
        ...

    @property
    def is_weekend(self) -> bool:
        ...

    @property
    def short_date(self) -> str:
        '''02/09/2003'''
        ...

    def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        ...

    def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        ...

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        ...

    def __eq__(self, other: Date) -> bool:
        ...

    def __gt__(self, other: Date) -> bool:
        ...

    def __lt__(self, other: Date) -> bool:
        ...
