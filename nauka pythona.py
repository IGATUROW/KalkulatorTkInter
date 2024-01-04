class Planet:
    def __init__(self, name, distance_from_sun, is_real):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.is_real = is_real

    def display_info(self):
        print(f"Planeta: {self.name}")
        print(f"Odległość od Słońca: {self.distance_from_sun:.2f} tys. km")
        if self.is_real == True:
            print(f"{self.name} jest planetą rzeczywistą\n")
        else:
            print(f"{self.name} jest planetą nierzeczywiastą")


def main():
    # Utworzenie listy planet
    planets_data = [
        ("Wulkan", 0.03, False),
        ("Merkury", 0.38, True),
        ("Wenus", 0.72, True),
        ("Ziemia", 1.0, True),
        ("Mars", 1.52, True),
        ("Faeton", 2.7, False),
        ("Jowisz", 5.2, True),
        ("Saturn", 9.53, True),
        ("Uran", 19.19, True),
        ("Neptun", 30.06, True),
        ("Pluton", 39.48, True),  # Zakładam, że Pluton jest traktowany jako planeta (true)
    ]

    planets = [Planet(name, distance * 149597870700 / 1000, is_real) for name, distance, is_real in planets_data]

    # Wyświetlenie listy planet
    for planet in planets:
        planet.display_info()

    # Pytanie do ostatniej pozycji w tabeli (Pluton)
    print("Czy Pluton jest uznawany za planetę?")

    # Podział na rzeczywiste i nie-rzeczywiste planety
    real_planets = [planet for planet in planets if planet.is_real]
    non_real_planets = [planet for planet in planets if not planet.is_real]

    # Wyświetlenie list planet rzeczywistych i nie-rzeczywistych
    print("\nRzeczywiste planety:")
    for planet in real_planets:
        planet.display_info()

    print("\nNie-rzeczywiste planety:")
    for planet in non_real_planets:
        planet.display_info()

    # Zapis do pliku
    filename = "planets_data.txt"
    with open(filename, "w") as file:
        for planet in planets:
            file.write(f"{planet.name},{planet.distance_from_sun},{planet.is_real}\n")

    # Odczyt danych z pliku i utworzenie obiektów
    read_planets = []
    with open(filename, "r") as file:
        for line in file:
            name, distance, is_real = line.strip().split(',')
            read_planets.append(Planet(name, float(distance), bool(is_real)))

    # Wyświetlenie informacji o planetach wczytanych z pliku
    print("\nPlanety wczytane z pliku:")
    for planet in read_planets:
        planet.display_info()


if __name__ == "__main__":
    main()
