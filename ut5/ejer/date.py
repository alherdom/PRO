MONTHS = {
    1: ("enero", 31),
    2: ("febrero", 28),
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
        """Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        """
        self.day = day
        self.month = month
        self.year = year
        self.leap_year = False

    def is_leap_year(self) -> bool:
        if self.year % 4 == 0 and self.year % 100 != 0:
            return True
        if self.year % 400 == 0:
            return True
        return False

    def days_in_month(self) -> int:
        days_in_month = MONTHS[self.month][1]
        if self.is_leap_year() and self.month == 2:
            days_in_month += 1
        return days_in_month

    def qty_leap_years(self) -> int:
        """Cantidad de años bisiestos entre 1900 hasta el año anterior a la fecha marcada"""
        return (self.year - 1900) // 4

    def delta_days(self) -> int:
        """Número de días transcurridos desde el 1-1-1900 hasta la fecha"""
        delta_days = self.day
        days_in_previous_years = ((self.year - 1900) * 365) + (self.year - 1900) // 4
        for i in range(1, self.month):
            days_in_month = MONTHS[i][1]
            delta_days += days_in_month
        delta_days += days_in_previous_years
        return delta_days - 1

    def elapsed_days_in_current_year(self) -> int:
        elapsed_days = self.day
        for i in range(1, self.month):
            days_in_month = MONTHS[i][1]
            elapsed_days += days_in_month
        return elapsed_days

    def weekday(self) -> int:
        """día de la semana de la fecha (0 para domingo, ..., 6 para sábado).
        El 1-1-1900 fue domingo."""
        weekday = (self.delta_days() % 7) + 1
        return weekday

    def is_weekend(self) -> bool:
        if self.weekday() == 0 or self.weekday() == 6:
            return True
        return False

    def short_date(self) -> str:
        """02/09/2003"""
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __str__(self):
        """martes 2 de septiembre de 2003"""
        return f"{WEEKDAYS[self.weekday()]} {self.day} de {MONTHS[self.month][0]} de {self.year}"

    def __add__(self, other):
        new_date = self.day + other
        pass

    def __sub__(self, other):
        pass

    def __eq__(self, other):
        pass


date1 = Date(9, 5, 1992)
print(date1.is_leap_year())
print(date1.qty_leap_years())
print(date1.elapsed_days_in_current_year())
print(date1.days_in_month())
print(date1.short_date())
print(date1.delta_days())
print(date1.weekday())
print(date1.is_weekend())
print(date1)
# operador + suma días a la fecha
# operador - resta días a la fecha o calcula la diferencia entre dos fechas
# operador == dice si dos fechas son iguales
# operador > dice si una fecha es mayor que otra
# operador < dice si una fecha es menor que otra
