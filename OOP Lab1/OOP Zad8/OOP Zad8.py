class Planets:
    def __init__(self, name, distance_from_sun, is_real):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.is_real = is_real

    def dissplay_info(self):
        print(f"Planeta {self.name}")
        print(f"Odległość od Słońca {self.distance_from_sun:2f} tys. km")
        if self.is_real == True:
            print(f"{self.name} jest planetą rzeczywistą\n")
        else:
            print(f"{self.name} jest planetą nierzeczywiastą")

def main():
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
        ("Pluton", 39.48, True),
    ]

    planets = [Planets(name, distance * 149597870700 / 1000, is_real) for name, distance, is_real in planets_data]

    for planet in planets:
        planet.dissplay_info()