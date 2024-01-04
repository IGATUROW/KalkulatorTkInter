import math

class Rozmiar:
    def __init__(self, bok, srednica):
        self.bok = bok
        self.srednica = srednica

    def zmien_rozmiar(self, nowy_bok, nowa_srednica):
        self.bok = nowy_bok
        self.srednica = nowa_srednica

class Kształt:
    def __init__(self, nazwa):
        self.nazwa = nazwa

class Kwadrat(Kształt):
    def __init__(self, nazwa, bok):
        super().__init__(nazwa)
        self.rozmiar = Rozmiar(bok, bok)
        self.bok = bok

    def __str__(self):
        return f"{self.nazwa} o długości boku {self.rozmiar.bok}"

class Koło(Kształt):
    def __init__(self, nazwa, srednica):
        super().__init__(nazwa)
        self.rozmiar = Rozmiar(srednica, srednica)
        self.srednica = srednica

    def __str__(self):
        return f"{self.nazwa} o średnicy {self.rozmiar.srednica}"

# Przykłady użycia:

kwadrat = Kwadrat("Kwadrat", 5)
print(kwadrat)

kwadrat.rozmiar.zmien_rozmiar(7, 7)
print(kwadrat)

kolo = Koło("Koło", 3)
print(kolo)

kolo.rozmiar.zmien_rozmiar(4, 4)
print(kolo)