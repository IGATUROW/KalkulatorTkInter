class Konto:
    def __init__(self, user_name, account_number):
        self.user_name = user_name
        self.account_number = account_number

    def show_info(self):
        print(f"Użytkownik o nazwie {self.user_name} ma numer konta: {self.account_number}")

    def __repr__(self):
        return f"Konto(user_name={self.user_name}, account_number={self.account_number})"


class BusinessAccount(Konto):
    def __init__(self, user_name, account_number, pit_number, zus_number):
        super().__init__(user_name,account_number)
        self.pit_number = pit_number
        self.zus_number = zus_number
    def show_info_business(self):
        super().show_info()
        self.show_pit()
        self.show_zus()

    def __str__(self):
        return (f"BusinessAccount (user_name= {self.user_name}, account_number = {self.account_number}, "
                f"pit_number = {self.pit_number}, zus_number = {self.zus_number}")

    def __repr__(self):
        return (f"BusinessAccount(user_name={self.user_name}, account_number={self.account_number}, pit_number={self.pit_number}, "
                f"zus_number={self.zus_number})")

    def show_pit(self):
        print(f"{self.user_name} opłać PIT w wysokości: {self.pit_number}")

    def show_zus(self):
        print(f"{self.user_name} opłać ZUS w wysokości {self.zus_number}")

    def load_file(self):
        with open('business_users.txt', 'r') as business_users_file:
            content = business_users_file.read()
            for line in content.split('\n'):
                self.business_users.append(BusinessAccount(line))


class PrivateAccount(Konto):
    def __init__(self, user_name, account_number):
        super().__init__(user_name, account_number)

    def show_info(self):
        super().show_info()

    def __repr__(self):
        return f"PrivateAccount(user_name={self.user_name}, account_number={self.account_number})"

    def __str__(self):
        return f"PrivateAccount (user_name={self.user_name}, account_number={self.account_number})"