def sprawdzMail(mail):

    if '@' in mail:
        if '.' in mail:
            return 'Twój adres email to: ' + mail
        else:
            return input('Podaj poprawny adres: ')
    else:
        return input('Podaj poprawny adres: ')
mail=input('Podaj adres email: ')
print(sprawdzMail(mail))