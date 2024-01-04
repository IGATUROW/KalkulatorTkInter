def CzyAnagram(pierwsze_slowo,drugie_slowo):


    pierwsze_slowo_lista = list(pierwsze_slowo.replace(" ","").lower())
    pierwsze_slowo_lista.sort()

    drugie_slowo_lista = list(drugie_slowo.replace(" ","").lower())
    drugie_slowo_lista.sort()
    if pierwsze_slowo_lista==drugie_slowo_lista:
        return'Podane słowa to anagramy!'
    else:
        return'Podane slowa to nie anagramy!'

pierwsze_slowo=input("Podaj pierwsze słowo: ")
drugie_slowo= input("podaj drugie słowo: ")
print(CzyAnagram(pierwsze_slowo, drugie_slowo))