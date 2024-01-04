from tkinter import *
from tkinter import messagebox


def Klik():
    global okienko
    pytanie = messagebox.askquestion("Pytanko...", "Na pewno?")
    if pytanie == 'yes':
        okienko.destroy()

def bit():
    global śledzenie_etykietki, result
    result = 0
    for i in range (8):
        result += ((czekbatony[i].get()) * pow(2,i))
    śledzenie_etykietki.set(result)
    return




okienko  = Tk()
okienko.title("Bitowiec")
stan7 = IntVar()
c7 = Checkbutton(okienko, text= "7", variable= stan7, command=bit)
c7.grid(row= 0, column = 0)
c7.deselect()
stan6 = IntVar()
c6 = Checkbutton(okienko, text= "6", variable= stan6, command=bit)
c6.grid(row = 0, column = 1)
c6.deselect()
stan5 = IntVar()
c5 = Checkbutton(okienko, text= "5", variable= stan5, command=bit)
c5.grid(row = 0, column = 2)
c5.deselect()
stan4 = IntVar()
c4 = Checkbutton(okienko, text= "4", variable= stan4, command=bit)
c4.grid(row = 0, column = 3)
c4.deselect()
stan3 = IntVar()
c3 = Checkbutton(okienko, text= "3", variable= stan3, command=bit)
c3.grid(row = 0, column = 4)
c3.deselect()
stan2 = IntVar()
c2 = Checkbutton(okienko, text= "2", variable= stan2, command=bit)
c2.grid(row = 0, column = 5)
c2.deselect()
stan1 = IntVar()
c1 = Checkbutton(okienko, text= "1", variable= stan1, command=bit)
c1.grid(row = 0, column = 6)
c1.deselect()
stan0 = IntVar()
c0 = Checkbutton(okienko, text= "0", variable= stan0, command=bit)
c0.grid(row= 0, column = 7)
c0.deselect()
czekbatony = [stan0, stan1, stan2, stan3, stan4, stan5, stan6, stan7]


śledzenie_etykietki = IntVar()
etykietka = Label(okienko, textvariable= śledzenie_etykietki, height= 4, font= ("Arial", "30" ,"bold"), fg="blue")
etykietka.grid(row= 1, columnspan = 8)
