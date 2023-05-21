class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie_studenta = imie
        self.nazwisko_studenta = nazwisko
        self.numer_indeksu_studenta = numer_indeksu
        self.indeks = []
    def __str__(self):
        return self.imie_studenta +" "+self.nazwisko_studenta + " " + str(self.numer_indeksu_studenta)
    def dodaj_ocene(self, ocena):
        self.indeks.append(ocena)
    def srednia_ocen(self):
        if len(self.indeks)==0:
            return 0
        else:
            return sum(self.indeks)/len(self.indeks)
        

Student_Wiktoria = Student("Wiktoria", "Nitka", 12345)
Student_Wiktoria.dodaj_ocene(5.0)
Student_Wiktoria.dodaj_ocene(4.0)
Student_Wiktoria.dodaj_ocene(3.0)
Student_Wiktoria.dodaj_ocene(2.0)

print(Student_Wiktoria.srednia_ocen())



