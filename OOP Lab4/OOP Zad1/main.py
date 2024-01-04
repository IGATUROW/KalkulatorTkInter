import unittest


class Komentarz:
    def __init__(self, komentarz):
        self.komentarz = komentarz


class User1:
    def __init__(self, imie, nazwisko, adres_email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres_email = adres_email

class NormalUser(User1):
    def __init__(self, imie, nazwisko, adres_email):
        super().__init__(imie, nazwisko, adres_email)


class Administrator:
    def __init__(self, haslo, imie, nazwisko, adres_email):
        super().__init__(imie, nazwisko, adres_email)
        self.haslo = haslo

    def sprawdz_haslo(self, user_name):
        if self.haslo != "12345":
            return f"{self.user_name} nie jesteś administratorem i nie masz uprawnień do edytowania komentarzy"


class KomentarzeTest(unittest.TestCase):

    komentarz = Komentarz("Super produkt")
    user_name = User1("Jan", "Kowalski", "janek.kowalski@gmial.com")
    normal_user = NormalUser("Jan Nowak")
    admin = Administrator("12345", "Julian Król")
    Administrator.sprawdz_haslo(user_name)


def main():
    unittest.main()

if __name__ == "__main__":
    main()



    # Uzytkownik
    # ZwyklyUzytkownik
    # Administrator
    # Komentarze
    # sprawdz_uprawnienia
    # Interface