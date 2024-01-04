class Statystyka:
    def __init__(self, lista):
        self.lista = lista

    def suma(self, start=0, koniec=None):
        if koniec is None:
            koniec = len(self.lista)
        return sum(self.lista[start:koniec])

    def srednia(self):
        suma_elementow = self.suma()
        liczba_elementow = len(self.lista)
        if liczba_elementow == 0:
            return None
        return suma_elementow / liczba_elementow

    def mediana(self):
        posortowana_lista = sorted(self.lista)
        liczba_elementow = len(posortowana_lista)
        if liczba_elementow == 0:
            return None
        srodkowy_index = liczba_elementow // 2
        if liczba_elementow % 2 == 1:
            return posortowana_lista[srodkowy_index]
        else:
            srodkowy_index -= 1
            return (posortowana_lista[srodkowy_index] + posortowana_lista[srodkowy_index + 1]) / 2

    def minimum(self):
        if not self.lista:
            return None
        return min(self.lista)

    def maximum(self):
        if not self.lista:
            return None
        return max(self.lista)


statystyka_instancja = Statystyka([1, 2, 3, 4, 5, 6])


print(f"Suma: {statystyka_instancja.suma()}")
print(f"Średnia: {statystyka_instancja.srednia()}")
print(f"Mediana: {statystyka_instancja.mediana()}")
print(f"Minimum: {statystyka_instancja.minimum()}")
print(f"Maksimum: {statystyka_instancja.maximum()}")
