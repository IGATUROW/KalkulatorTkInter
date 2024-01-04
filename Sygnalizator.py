import tkinter as tk

# Funkcja do zmiany koloru świateł
def zmien_kolor():
    global aktualny_kolor
    tło.delete("wszystko")  # Czyści płótno

    if aktualny_kolor == "czerwony":
        aktualny_kolor = "czerwony + żółty"
        kolory_światło_czerwoneiżółte= ['red','yellow','gray']
        czerwonyiżółty = [tło.create_oval(100, 50 * ((i * 3) + 1), 200, 150 * (i + 1), fill=kolory_światło_czerwoneiżółte[i],tags="wszystko") for i in range(3)]
        okno.after(1000, zmien_kolor)  # Wywołuje funkcję zmien_kolor co 1000 ms (1 sekunda)
        return czerwonyiżółty

    elif aktualny_kolor == "czerwony + żółty":
        aktualny_kolor = "zielony"
        kolory_światło_zielone = ['gray','gray','green']
        zielony = [tło.create_oval(100, 50 * ((i * 3) + 1), 200, 150 * (i + 1), fill=kolory_światło_zielone[i],tags="wszystko") for i in range(3)]
        okno.after(1000, zmien_kolor)  # Wywołuje funkcję zmien_kolor co 1000 ms (1 sekunda)
        return zielony

    elif aktualny_kolor == "zielony":
        aktualny_kolor = "żółty"
        kolory_światło_żółte = ['gray','yellow','gray']
        żółty = [tło.create_oval(100, 50 * ((i * 3) + 1), 200, 150 * (i + 1), fill=kolory_światło_żółte[i],tags="wszystko") for i in range(3)]
        okno.after(1000, zmien_kolor)  # Wywołuje funkcję zmien_kolor co 1000 ms (1 sekunda)
        return żółty

    else:
        aktualny_kolor = "czerwony"
        kolory_światło_czerwone = ['red', 'gray','gray']
        czerwony = [tło.create_oval(100, 50*((i*3)+1), 200 , 150*(i+1), fill=kolory_światło_czerwone[i], tags="wszystko") for i in range(3)]
        okno.after(1000, zmien_kolor)
        return czerwony

# Inicjalizacja głównego okna
okno = tk.Tk()
okno.title("Sygnalizator")

# Płótno
tło = tk.Canvas(okno, width=300, height=500)
tło.pack()

aktualny_kolor = "czerwony"  # Początkowy kolor to czerwony
zmien_kolor()  # Rozpoczyna zmianę kolorów

okno.mainloop()

