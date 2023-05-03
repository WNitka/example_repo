# zadanie 1.1

# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student

hello = "Hello"
student = "Ola"

print(f'{hello} {student}')

# zadanie 1.2

student = input("Enter your name:")
print(f'{hello} {student}')

# zadanie 1.3

# policz liczbe studentow w tablicy studenci 
# oczekiwany rezultat: Liczba studentow wynosi: 4

studenci = ["Ania", "Kuba", "Piotr", "Jan"]

liczba_studentów = len(studenci)

print(f'Liczba studentów wynosi: {liczba_studentów}')

# zadanie 1.4

# za pomoca petli i print przywitaj sie z kazdym studentem
# z tabeli studenci osobno
# oczekiwany rezultat:
# Hello Ania
# Hello Kasia
# Hello Piotr
# Hello Tomek

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for i in studenci:
    print(f'Hello {i}')

# zadanie 1.5

# oczekiwany rezultat:
# Wynik wynosi: 81

liczba = 3
potega = 4

wynik = 3**4
print(f'Wynik wynosi: {wynik}')


# zadanie 1.6

# policz ilosc nawiasow ( w danym ciagu znakow
# oczekiwany rezultat:
# Liczba nawiasow otwierajacych wynosi: 4
ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count('(')

print(f'Liczba nawiasow otwierajacych wynosi: {liczba_nawiasow_otwierajacych}')

# zadanie 1.7

# posortuj alfabetycznie (od imienia) studentow
# oczekiwany rezultat:
# Anna Szczesny
# Barbara Kowalska
# Jan Niezbedny
# Tomasz Nijaki

studenci = ["Anna Szczesny", "Tomasz Nijaki",
            "Barbara Kowalska", "Jan Niezbedny"]

def sortowaniePoImieniu(inputList):
    k=[]
    inputList.sort()
    for i in inputList:
        k.append(i)
    return k

posortowaniImie = sortowaniePoImieniu(studenci)


print(f"Alfabetyczna lista studentow wynosi: {posortowaniImie}")


# zadanie 1.8

# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki",
            "Barbara Kowalska", "Jan Niezbedny"]

def sortowaniePoNazwisku(inputList):
    inputList.sort(key=lambda k: k.split()[-1])
    return inputList
   

posortowaniNazwisko = sortowaniePoNazwisku(studenci)

print(f"Alfabetyczna lista studentow wynosi: {posortowaniNazwisko}")


#zadanie 1.9

# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

def liczenieStudentow(a):
    k = []          
    for student in a:
        x = student.count("N")
        k.append(x)
    return sum(k)
    

liczba_n = liczenieStudentow(studenci)

print(f"Liczba studentow na N wynosi: {liczba_n}")

# zadanie 1.10

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

class wykresLiniowy:
   def zbadajWykres(self, punkty):
      (x0, y0), (x1, y1) = punkty[0], punkty[1]
      for i in range(2, len(punkty)):
         x, y = punkty[i]
         if (x0 - x1) * (y1 - y) != (x1 - x) * (y0 - y1):
            return False
      return True
   
wynik = wykresLiniowy()

wykres_1_funkcja_liniowa = wynik.zbadajWykres(wykres_1)
wykres_2_funkcja_liniowa = wynik.zbadajWykres(wykres_2)
wykres_3_funkcja_liniowa = wynik.zbadajWykres(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")