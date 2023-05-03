# zadanie 1.1

hello = "Hello"
student = "Ola"

# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
print(f'{hello} {student}')

# zadanie 1.2

student = input("Enter your name:")
print(f'{hello} {student}')

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentów = len(studenci)

print(f'Liczba studentów wynosi: {liczba_studentów}')

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for i in studenci:
    print(f'Hello {i}')

# za pomoca petli i print przywitaj sie z kazdym studentem
# z tabeli studenci osobno
# oczekiwany rezultat:
# Hello Ania
# Hello Kasia
# Hello Piotr
# Hello Tomek

# zadanie 1.5

liczba = 3
potega = 4

wynik = 3**4
print(f'Wynik wynosi: {wynik}')
# oczekiwany rezultat:
# Wynik wynosi: 81

# zadanie 1.6

# policz ilosc nawiasow ( w danym ciagu znakow

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count('(')

# oczekiwany rezultat:
# Liczba nawiasow otwierajacych wynosi: 4
print(f'Liczba nawiasow otwierajacych wynosi: {liczba_nawiasow_otwierajacych}')

# zadanie 1.7

# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki",
            "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.8

# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki",
            "Barbara Kowalska", "Jan Niezbedny"]

def sortowaniePoNazwisku(inputList):
    inputList.sort(key=lambda k: k.split()[-1])
    return inputList
   

sortowaniePoNazwisku(studenci)

print("Alfabetyczna lista studentow wynosi: " )
for student in studenci:
    print(student)

