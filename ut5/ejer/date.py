START_YEAR = 1900
FINAL_YEAR = 2050
MONTHS = {
    1: ("enero", 31),
    2: ("febrero", 28, 29),
    3: ("marzo", 31),
    4: ("abril", 30),
    5: ("mayo", 31),
    6: ("junio", 30),
    7: ("julio", 31),
    8: ("agosto", 31),
    9: ("septiembre", 30),
    10: ("octubre", 31),
    11: ("noviembre", 30),
    12: ("diciembre", 31),
}
WEEKDAYS = {
    0: "domingo",
    1: "lunes",
    2: "martes",
    3: "miércoles",
    4: "jueves",
    5: "viernes",
    6: "sábado",
}

class Date:
    def __init__(self, day: int, month: int, year: int):
        """validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        """
        self.day = day
        self.month = month
        self.year = year
        if not (START_YEAR <= year <= FINAL_YEAR):
            self.year = START_YEAR
        if not (1 <= month <= 12):
            self.month = 1
        if not (1 <= day <= self.days_in_month()):
            self.day = 1

    def is_leap_year(self) -> bool:
        if (self.year % 4 == 0 and self.year % 100 != 0) or self.year % 400 == 0:
            return True
        return False
        
    def days_in_month(self) -> int:
        """número de días en el mes actual"""
        if self.month == 2 and self.is_leap_year():
            return MONTHS[self.month][2]
        return MONTHS[self.month][1]

    def qty_leap_years(self) -> int:
        """cantidad de años bisiestos entre 1900 hasta el año anterior a la fecha marcada"""
        return (self.year - 1900) // 4
    
    def elapsed_days_in_current_year(self) -> int:
        """número de días transcurridos en el año actual"""
        return sum(MONTHS[i][1] for i in range(1, self.month)) + self.day
    
    def delta_days(self) -> int:
        """número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        days_in_previous_years = (self.year - 1900) * 365 + self.qty_leap_years()
        return days_in_previous_years + self.elapsed_days_in_current_year() - 1

    def weekday(self) -> int:
        """día de la semana de la fecha (de 0: domingo a 6: sábado).
        El 1-1-1900 fue domingo."""
        weekday = (self.delta_days() + 1) % 7
        return weekday if weekday != 7 else 0

    def is_weekend(self) -> bool:
        return self.weekday() in [0, 6]

    def short_date(self) -> str:
        """02/09/2003"""
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __str__(self) -> str:
        """martes 2 de septiembre de 2003"""
        return f"{WEEKDAYS[self.weekday()]} {self.day} de {MONTHS[self.month][0]} de {self.year}"
    
    def __add__(self, days_to_add) -> str:
        """operador + suma de días a la fecha marcada"""
        self.day += days_to_add
        while self.day > self.days_in_month():
            self.day -= self.days_in_month()
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1          
        return f"{self.day}/{self.month}/{self.year}"

    def __sub__(self, days_to_sub) -> str: # Y restando una fecha?
        """operador - resta de días a la fecha marcada"""
        self.day -= days_to_sub
        while self.day < 1:
            self.day += self.days_in_month()
            self.month -= 1
            if self.month < 1:
                self.month = 12
                self.year -= 1
        return f"{self.day}/{self.month}/{self.year}"

    def __eq__(self, other) -> bool:
        """operador == dice si dos fechas son iguales"""
        if self.delta_days() == other.delta_days():
            return True
        return False
    
    def __lt__(self, other) -> bool:
        """operador < dice si una fecha es menor que otra"""
        if self.delta_days() < other.delta_days():
            return True
        return False
    
    def __gt__(self, other) -> bool:
        """operador > dice si una fecha es mayor que otra"""
        if self.delta_days() > other.delta_days():
            return False
        return False    

date1 = Date(29, 2, 1993)
date2 = Date(11, 4, 2023)
date3 = Date(11, 4, 2023)
print(date1.is_leap_year())
print(date1.qty_leap_years())
print(date1.elapsed_days_in_current_year())
print(date1.days_in_month())
print(date1.short_date())
print(date1.delta_days())
print(date1.weekday())
print(date1.is_weekend())
print(date1)
print(date1 - 10)
print(date2 == date3)
print(date2 > date3)
print(date2 < date3)