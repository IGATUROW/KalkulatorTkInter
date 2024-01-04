def is_palidrom(słowo):
    if słowo == słowo[::-1]:
        return'To słowo jest palidromem'
    else:
        return'Słowo nie jest palidromem.'
słowo=input('Podaj słowo,aby sprawdzić,czy jest palidromem: ')
print(is_palidrom(słowo))