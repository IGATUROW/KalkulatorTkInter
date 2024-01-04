import random

# Lista haseł do odgadnięcia
hasla = ["python", "wisielec", "programista", "komputer", "inteligencja"]

# Funkcja losująca hasło z listy
def losuj_haslo():
    return random.choice(hasla)

# Funkcja rysująca wisielca
def rysuj_wisielca(bledy):
    # Wyświetlenie rysunku wisielca na podstawie liczby błędów
    wisielec = [
        "  ____\n  |  |\n     |\n     |\n     |\n     |\n",
        "  ____\n  |  |\n  O  |\n     |\n     |\n     |\n",
        "  ____\n  |  |\n  O  |\n /|  |\n     |\n     |\n",
        "  ____\n  |  |\n  O  |\n /|\\ |\n     |\n     |\n",
        "  ____\n  |  |\n  O  |\n /|\\ |\n /   |\n     |\n",
        "  ____\n  |  |\n  O  |\n /|\\ |\n / \\ |\n     |\n"
    ]
    return wisielec[bledy]

# Funkcja do obsługi gry Wisielec
def wisielec():
    print("Witaj w grze Wisielec!")
    haslo = list(losuj_haslo().upper())
    dlugosc_hasla = len(haslo)
    odgadniete_litery = ['_'] * dlugosc_hasla
    bledy = 0

    while True:
        print(rysuj_wisielca(bledy))
        print(" ".join(odgadniete_litery))

        if bledy == 6:
            print("Przegrałeś! Hasło to: " + "".join(haslo))
            break

        if '_' not in odgadniete_litery:
            print("Gratulacje! Wygrałeś!")
            break

        litera = input("Podaj literę: ").upper()

        if len(litera) != 1 or not litera.isalpha():
            print("Proszę podać pojedynczą literę.")
            continue

        if litera in haslo:
            for i in range(dlugosc_hasla):
                if haslo[i] == litera:
                    odgadniete_litery[i] = litera
        else:
            print("Nie ma takiej litery w haśle.")
            bledy += 1

if __name__ == "__main__":
    wisielec()