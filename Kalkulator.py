from tkinter import *
import tkinter.messagebox as message

def licz():
    global choosen_op, lewa_wartość, prawa_wartość, pole_lewe, pole_prawe
    lewe = lewa_wartość.get()
    prawe = prawa_wartość.get()
    op = choosen_op.get()

    if len(lewe) == 0:
        message.showerror("error", "Lewe pole jest puste!")
        pole_lewe.focus_set()
        return

    if len(prawe) == 0:
        message.showerror("error", "Prawe pole jest puste!")
        pole_prawe.focus_set()
        return

    if not prawe.isdigit():
        message.showerror("error", "W prawym polu znajdują się inne znaki niż cyfry.")
        pole_prawe.focus_set()
        return

    if not lewe.isdigit():
        message.showerror("error", "W lewym polu znajdują się inne znaki niż cyfry.")
        pole_prawe.focus_set()
        return

    if op == 3 and int(prawe) == 0:
        message.showerror("error", "Dzielenie przez zero.")
        pole_prawe.focus_set()
        return

    if not (1 <= op <= 4):
        message.showerror("error", "Nie zaznaczyłeś żadnej z operacji.")
        return

    if op == 1:
        result = int(lewe) + int(prawe)
    elif op ==2:
        result = int(lewe) - int(prawe)
    elif op == 3:
        result = int(lewe) / int(prawe)
    elif op == 4:
        result = int(lewe) * int(prawe)

    message.showinfo("Wynik", f"Wynik = {result}")



o = Tk()
o.title("Kalkulatorek")



#Pola do wprowadzania danych
lewa_wartość = StringVar()
pole_lewe = Entry(o, textvariable = lewa_wartość)
pole_lewe.grid(row = 2, column = 0)

prawa_wartość = StringVar()
pole_prawe = Entry(o, textvariable = prawa_wartość)
pole_prawe.grid(row = 2, column = 2)

#Radiobuttony
choosen_op = IntVar()
plus = Radiobutton(o, text= "+", variable = choosen_op, value= 1)
plus.grid(row = 0, column = 1)
minus = Radiobutton(o, text= "-", variable= choosen_op, value= 2)
minus.grid(row = 1, column = 1)
podzielić = Radiobutton(o, text= "/", variable= choosen_op, value= 3)
podzielić.grid(row = 2, column = 1)
pomnożyć = Radiobutton(o, text= "*", variable= choosen_op, value= 4)
pomnożyć.grid(row = 3, column = 1)
oblicz = Button(o, text= "Oblicz!", command= licz)
oblicz.grid(row = 4, column = 1)

o.mainloop()