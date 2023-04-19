from __future__ import annotations
INITIAL_YEAR, FINAL_YEAR = 1900, 2050
MONTHS_NAMES = {
    1: "ENERO",
    2: "FEBRERO",
    3: "MARZO",
    4: "ABRIL",
    5: "MAYO",
    6: "JUNIO",
    7: "JULIO",
    8: "AGOSTO",
    9: "SEPTIEMBRE",
    10: "OCTUBRE",
    11: "NOVIEMBRE",
    12: "DICIEMBRE"
}
WEEKDAYS_NAMES = {
    0: "DOMINGO",
    1: "LUNES",
    2: "MARTES",
    3: "MIERCOLES",
    4: "JUEVES",
    5: "VIERNES",
    6: "SABADO"
}
class Date:
    def __init__(self, day: int, month: int, year: int):
        self.year = year if INITIAL_YEAR <= year <= FINAL_YEAR else INITIAL_YEAR
        self.month = month if 1 <= month <= 12 else 1
        self.day = day if 1 <= day <= Date.static_days_in_month(self.month, self.year) else 1
    
    @staticmethod
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def days_of_first_approach(self) -> int:
        return (self.year - INITIAL_YEAR) * 365
    
    def qty_of_leap_years(self) -> int:
        return sum(1 for i in range(INITIAL_YEAR, self.year) if Date.is_leap_year(i))

    def days_elapsed_in_year(self) -> int:
        return sum(Date.static_days_in_month(self.year, i) for i in range(1, self.month)) + self.day
    
    def get_delta_days(self):
        return self.days_of_first_approach() + self.qty_of_leap_years() + self.days_elapsed_in_year() - 1
    
    @staticmethod
    def static_days_in_month(year: int, month: int) -> int:
        if month == 2:
            return 29 if Date.is_leap_year(year) else 28
        return 30 if month in [4,6,9,11] else 31

    @property
    def days_in_month(self) -> int:
        return Date.static_days_in_month(self.year, self.month)

    @property
    def weekday(self) -> int:
        return (self.get_delta_days() + 1) % 7
       
    @property
    def is_weekend(self) -> bool:
        return self.weekday in [0, 6]

    @property
    def short_date(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __str__(self):
        return f"{WEEKDAYS_NAMES[self.weekday]} {self.day} DE {MONTHS_NAMES[self.month]} DE {self.year}"

    def __add__(self, days: int) -> Date:
        new_day = self.day + days
        new_month, new_year = self.month, self.year
        while new_day > Date.static_days_in_month(new_year, new_month):
            new_day -= Date.static_days_in_month(new_year, new_month)
            new_month += 1
            if new_month > 12:
                new_month = 1
                new_year += 1
        return Date(new_day, new_month, new_year)

    def __sub__(self, other: Date | int) -> int | Date:
        if isinstance(other, int):
            new_day = self.day - other
            new_month, new_year = self.month, self.year
            while new_day < 0:
                new_day += Date.static_days_in_month(new_year, new_month)
                new_month -= 1
                if new_month == 0:
                    new_month = 12
                    new_year -= 1
            return Date(new_day, new_month, new_year)

        if isinstance(other, Date):
            return abs(self.get_delta_days() - other.get_delta_days())

    def __eq__(self, other: Date) -> bool:
        return self.get_delta_days() == other.get_delta_days()

    def __gt__(self, other: Date) -> bool:
        return self.get_delta_days() > other.get_delta_days()

    def __lt__(self, other: Date) -> bool:
        return self.get_delta_days() < other.get_delta_days()