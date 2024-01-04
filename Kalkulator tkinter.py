import tkinter as tk

symbols = ['7', '8', '9', '/', '\u21BA', 'C', '4', '5', '6', '*', '(', ')', '1', '2', '3', '-', 'x^2', '\u221A', '0', ',', '%', '+']


def create_window():
    root = tk.Tk()
    root.geometry('460x387')
    root.title('Kalkulator')

    return root


def create_screen(root):
    screen = [tk.Label(root, bg = 'light gray', width = 64, anchor = 'w', borderwidth = 2) for i in range(3)]

    for i in range(len(screen)):
        screen[i].grid(row=i, columnspan = 6, ipady=15, ipadx=1)

    return screen


def calculations(root, screen):

    calculation_field = tk.Entry(root, borderwidth=0, highlightcolor='white', highlightbackground='white')
    calculation_field.grid(row=len(screen), columnspan = 6,  ipadx = 166, ipady = 10)

    info = tk.Label(root, bg='white', width=64, anchor='w', borderwidth = 2)
    info.grid(row=len(screen) + 1, columnspan = 6, ipady=15, ipadx=1)

    return calculation_field, info


def on_button_click(calculation_field, symbol):

    def f():

        if symbol == '\u21BA':
            bufor = calculation_field.get()[:-1]
            calculation_field.delete(0, tk.END)
            calculation_field.insert(0, bufor)

        elif symbol == 'C':
            calculation_field.delete(0, tk.END)
            info['text'] = ''

        else:
            tekst = symbol if symbol != 'x^2' else '^2'
            calculation_field.insert(tk.END, tekst)
            info['text'] = ''

    return f


def count(calculation_field, screen, info):

    def text_correct(tekst):
        i= 1
        while tekst[-i] == ')':
            i+=1

        return tekst[-i].isdigit()

    def multiple_operators(tekst):

        for i in range(len(tekst)):
            if not tekst[i].isdigit() and not tekst[i+1].isdigit():
                return True

        return False

    def replace_exponent_sign(tekst):
        for i in range(len(tekst)):
            if tekst[i] == '^':
                tekst = tekst[:i] +'**'+ tekst[i+1:]
        return tekst

    def f():
        tekst = calculation_field.get()
        if not text_correct(tekst) or multiple_operators(tekst):
            info['text'] = 'Błędne wyrażenie'

        else:
            for i in range(1, len(screen)):
                if screen[i]['text']:
                    screen[i-1]['text'] = screen[i]['text']

            if '^' in tekst:
                expression = replace_exponent_sign(tekst)
                screen[-1]['text'] = tekst + ' = ' + str(eval((expression)))

            else:
                screen[-1]['text'] = tekst + ' = ' + str(eval((tekst)))
                calculation_field.delete(0, tk.END)
    return f

def create_buttons(root, screen):

    buttons = [tk.Button(root, text=symbol, borderwidth=0) for symbol in symbols]

    j = len(screen) + 2
    for i in range(len(buttons)):
        if i % 6 == 0:
            j += 1

        margin = 28 if len(symbols[i]) == 1 else 22
        buttons[i].grid(row = j, column = i % 6, ipady  = 5, ipadx = margin)
        buttons[i].configure(command = on_button_click(calculation_field, buttons[i]['text']))

    equal_sign = tk.Button(root, text='=', bg='#FFD1DC', borderwidth=0, command= count(calculation_field, screen, info))
    equal_sign.grid(row=len(screen) + 6, column=4, columnspan=2, ipady=7, ipadx=66)

    return buttons


if __name__ == '__main__':
    root = create_window()

    screen = create_screen(root)

    calculation_field, info = calculations(root, screen)

    buttons = create_buttons(root, screen)

    root.mainloop()