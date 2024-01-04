class GeometricFigure:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Figura {self.name}")
        print(f"Położenie {self.position}")


def main():
    figure1 = GeometricFigure("Koło", (2,3))
    figure1.display_info()
    figure2 = GeometricFigure("Kwadrat", (3,6))
    figure2.display_info()

if __name__ == "__main__":
    main()