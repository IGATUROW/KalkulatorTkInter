Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Hangman
... #
... # Klasyczna gra zwana również Szubienicą. Komputer wybierze słowo losowo,
... # a gracz spróbuje odgadnąć poszczególne litery.
... # Jeśli graczowi nie uda się w porę odgadnąć słowa, ludzik zostanie powieszony.
... 
... # import modułów
... 
... import random
... 
... # stałe
... HANGMAN = (
... """
... ______
... |   |
... |
... |
... |
... |
... |
... |
... |
... ----------
... """,
... """
... ______
... |   |
... |   0
... |
... |
... |
... |
... |
... |
... ----------
... """,
... """
... ______
... |   |
|   0
|  /|\\
|
|
|
|
|
----------
""",
"""
______
|   |
|   0
|  /|\\
|  / \\
|
|
|
|
----------
""")
MAX_ZLE= len(HANGMAN) - 1
SLOWA = ("KAPITAŁ","MORZE","KOMPUTER","ZABAWA","SZUBIENICA","EGZAMIN")

# inicjalizacja zmiennych
slowo_do_odgadniecia = random.choice(SLOWA)         # słowo do odgadnięcia
juz_blisko = "-" * len(slowo_do_odgadniecia)        # kreska zastępuje nieodgadniętą literę
zle = 0                                             # liczba nietrafionych liter
uzyte_litery = []                                   # litery już użyte w zgadywniu

print("Witaj w grze wisielec! Powodzenia!")

while zle < MAX_ZLE and juz_blisko != slowo_do_odgadniecia:
    print(HANGMAN[zle])                                                     # Aktualna postać ludzika
    print("\nWykorzystałeś już następujące litery:\n", uzyte_litery)        # Lista liter, których gracz użył
    print("\nNa razie zgadywane słowo wygląda tak:\n", juz_blisko)          # Tak wygląda częściowo odgadnięte słowo

    pytanie = input("Wprowadź literę: ")                    # Pobieranie litery od użytkownika
    pytanie = pytanie.upper()                               # Zamiana litery na wielką

    while pytanie in uzyte_litery:                          # Sprawdzenie, czy użytkownik nie podał już danej litery.
        print("Już wykorzystałeś literę ", pytanie)         # Ewentualna prośba o podanie innej,
        pytanie = input("Wprowadż literę: ")                # jeszcze nie użytej litery
        pytanie = pytanie.upper()

    uzyte_litery.append(pytanie)

    if pytanie in slowo_do_odgadniecia:                     # Sprawdzenie, czy podana litera jest w zgadywanym słowie.
        print("\nTak!", pytanie, "znajduje się w zgadywanym słowie!") # Jest w danym słowie.

    # utworzenie nowej wersji juz_blisko, z odgadniętą literą
        nowa = ""
        for i in range(len(slowo_do_odgadniecia)):
            if pytanie == slowo_do_odgadniecia[i]:
                nowa += pytanie
            else:
                nowa += juz_blisko[i]
        juz_blisko = nowa

    else:                                                              # Podanej litery nie ma w zgadywanym słowie
        print("\nNiestety,", pytanie, "nie występuje w zgadywanym słowie.")
        zle += 1

if zle == MAX_ZLE:
    print(HANGMAN[zle])
    print("\nLudzik został powieszony!")
else:
    print("\nOdgadłeś!")

print("\nZagadkowe słowo to ", slowo_do_odgadniecia)

