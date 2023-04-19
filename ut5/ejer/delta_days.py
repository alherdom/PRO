def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 30 if month in [4,6,9,11] else 31

def days_in_currect_year(day, month, year):
    return sum(days_in_month(year, i) for i in range(1, month)) + day

def delta_days(dia, mes, año):
    dias_años_transcurridos = (año - 1900) * 365
    dias_años_bisiestos = sum(1 for i in range(1900, año) if is_leap_year(i))
    dias_año_actual = days_in_currect_year(dia, mes, año)
    return dias_años_bisiestos + dias_años_transcurridos + dias_año_actual - 1

print(delta_days(1, 3, 1979))

print(days_in_currect_year(1,3,1979))

