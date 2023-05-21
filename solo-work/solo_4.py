import random
from statistics import mean 
class Plyta:
    def __init__(self, wykonawca, nazwa_albumu, lista_piosenek, rok_wydania, kraj, gatunek, liczba_piosenek, ocena_krytykow):
        self.wykonawca = wykonawca
        self.nazwa_albumu = nazwa_albumu
        self.lista_piosenek = list(lista_piosenek)
        self.rok_wydania = rok_wydania
        self.kraj = kraj
        self.gatunek = gatunek
        self.liczba_piosenek = liczba_piosenek
        self.ocena_krytykow = []
    def __str__(self):
        return self.wykonawca + " " + self.nazwa_albumu + " " + str(self.rok_wydania) + " " + self.gatunek +" " + self.kraj
    def przykladowa_piosenka(self):
        przykladowaPiosenka = random.choice(self.lista_piosenek)
        return(f"Album {self.nazwa_albumu} zawiera {self.liczba_piosenek} na przykład {przykladowaPiosenka}")
    def dodaj_recenzje(self,recenzja):
        self.ocena_krytykow.append(recenzja)
    def srednia_ocena_krytykow(self):
        if len(self.ocena_krytykow)==0:
            return 0
        else:
            return mean(self.ocena_krytykow)

   
piosenki = ["Fly to my room", "Stay", "Life goes on", "Telepathy", "Blue&grey","Dis-ease", "Dynamite"]
Plyta_BE = Plyta("BTS","BE",piosenki, 2020, "Korea Południowa","pop", 7, "BigHitEnt")

Plyta_BE.dodaj_recenzje(10.0)
Plyta_BE.dodaj_recenzje(9.0)
Plyta_BE.dodaj_recenzje(7.0)
Plyta_BE.dodaj_recenzje(9.0)
Plyta_BE.dodaj_recenzje(10.0)

print(Plyta_BE.srednia_ocena_krytykow())