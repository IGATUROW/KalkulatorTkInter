from tkinter import *


okno = Tk()
okno.geometry("400x300")

def Tabliczka():
    global mnozna_var, mnoznik_var, result_label

    mnoznik_var = StringVar()
    mnoznik_var.set("1")

    mnozna_var = StringVar()
    mnozna_var.set("1")

    result_label = Label(okno, text="", font=("Arial", 38))
    result_label.grid(rowspan = 10, columnspan = 10)

    for i in range(10):
        mnoznik = Radiobutton(okno, text = f"{i+1}", variable = mnoznik_var, value = str(i+1), command = update_result)
        mnoznik.grid(row = i, column = 0)

        mnozna = Radiobutton(okno, text = f"{i+1}", variable = mnozna_var, value = str(i+1), command = update_result)
        mnozna.grid(row = 0, column = i+1)


def update_result():
    try:
        mnoznik = int(mnoznik_var.get())
        mnozna = int(mnozna_var.get())
        result = mnoznik * mnozna
        result_label.config(text = f"{result}", fg = "green")
    except ValueError:
        pass


Tabliczka()
okno.mainloop()