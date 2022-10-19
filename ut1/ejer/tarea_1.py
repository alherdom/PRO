# 1. Escriba un programa en Python que acepte el radio de un
#  circulo y compute su área.
# Area = Pi * r^2
PI = 3.141592
Radio = 5
Radio2 = Radio**2
Area = PI * Radio2
print("The area of circle is equal to:")
print(Area)
# 2. Escriba un programa en Python que acepte el radio de una
# esfera y obtenga su volumen.
# Volumen = 4/3 * Pi * r^3
Radio = 5
Radio3 = Radio**3
Volumen = (4/3) * PI * Radio3
print("The volumen of a sphere is equal to:")
print(Volumen)
# 3. Escriba un programa en Python que acepte la base y la altura de un
# triángulo y compute su área.
# Area = Base * Altura / 2
Base = 4
Height = 5
Area = (Base * Height) / 2
print("The area of triangle is equal to:")
print(Area)
# 4. Escriba un programa en Python que compute el futuro valor de una cantidad
# de dinero, a partir del capital inicial, tipo de interés y número de años.
Capital = 10000
Interest = 3.5
Years = 7
Int_Conv = Interest/100
Calc_Int = Capital * Int_Conv * Years
Future_Value = Calc_Int + Capital
print("The future value of capital is equal to:")
print(Future_Value)
# 5. Escriba un programa en Python que calcule la distancia entre dos puntos
# (X1,Y1) y (X2,Y2)
X1 = 3
Y1 = 5
X2 = -7
Y2 = -4
Oper_1 = (X2 - X1) ** 2
Oper_2 = (Y2 - Y1) ** 2
Oper_3 = Oper_1 + Oper_2
Distance = Oper_3 ** (1/2)
print("The euclidean distance is equal to:")
print(Distance)