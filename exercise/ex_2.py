import math

#Trojkat
a = 10
b = 20
c = 15
h = 12

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) +
      ", zas pole wynisi " + str(pole) + ".")
#Prostokat
a = 10
b = 20

obwod_prostokat = a+b+a+b
pole_prostokat = a*b
print("Obwod prostokata wynosi " + str(obwod_prostokat) +
      ", zas pole wynisi " + str(pole_prostokat) + ".")

#Kolo

r = 10
pi = math.pi

obwod_kolo = 2*pi*r
pole_kolo = pi*r**2

print("Obwod kola wynosi " + str(obwod_kolo) +
      ", zas pole wynisi " + str(pole_kolo) + ".")
