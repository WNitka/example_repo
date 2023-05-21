import math

def trojkat(bok_a,bok_b,bok_c,h_a):
    pole = bok_a * h_a/2
    obwod = bok_a + bok_b + bok_c
  
    return pole,obwod

print(f'Pole i obwod trojkąta wynosi: {trojkat(10,15,12,8)}')

def trapez (bok_1,bok_2,bok_3,bok_4,h_a):
    pole = 0.5*(bok_1+bok_2)*h_a
    obwod = bok_1+bok_2 +bok_3+bok_4
    return pole, obwod
print(f'Pole i obwod trapeza wynosi: {trapez(10,15,12,8,4)}')

def kolo (promien):
    pi = math.pi
    pole = pi*promien**2
    obwod = 2*pi*promien
    return pole, obwod
print(f'Pole i obwod pola wynosi: {kolo(4)}')
