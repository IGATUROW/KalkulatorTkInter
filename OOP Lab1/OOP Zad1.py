class NameSurname:
    def __init__(self,imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def pokaz(self):
        print(self.imie, " ", self.nazwisko)


obiekt1 = NameSurname('Jan', 'Kowalski')
obiekt2 = NameSurname('Antoni', 'Nowak')
obiekt3 = NameSurname('Janina', 'Lewandowska')


obiekt1.pokaz()
obiekt2.pokaz()
obiekt3.pokaz()