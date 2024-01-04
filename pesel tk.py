from tkinter import *
from tkinter import messagebox

def validate_pesel(pesel):
    if len(pesel) != 11:
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    check_sum = 0

    for i in range(10):
        check_sum += int(pesel[i]) * weights[i]

    check_digit = (10 - (check_sum % 10)) % 10

    return check_digit == int(pesel[10])

def check_pesel():
    user_pesel = wpis.get()
    if validate_pesel(user_pesel):
        messagebox.showinfo("Wynik", "PESEL jest poprawny.")
    else:
        messagebox.showerror("Wynik", "PESEL jest niepoprawny.")

okienko = Tk()
okienko.title("tk")
tx = StringVar()  # Utworznie zmiennej śledzonej
etykietka = Label(okienko, text="PESEL:")
etykietka.grid(row=0, column=0)
guzik = Button(okienko, text="Sprawdź!", command=check_pesel)
guzik.grid(row=1, columnspan=2)
wpis = Entry(okienko, width=11, textvariable=tx)
wpis.grid(row=0, column=1)

wpis.focus_set()
okienko.mainloop()