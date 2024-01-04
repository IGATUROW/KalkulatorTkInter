from tkinter import *

okno = Tk()
c = Canvas(okno, width= 600, height=600, bg= 'white')
c.create_polygon(400,150,500,200,400,250, outline='red', width= 2, fill='white')
c.create_polygon(400,250,500,300,400,350, outline='red', width= 2, fill='white')
c.create_rectangle(380,100,400,500, outline= 'red', width= 2, fill='white')
c.create_rectangle(230,100,250,200, outline= 'red', width= 2, fill='white')
c.create_rectangle(230,350,250,500, outline= 'red', width= 2, fill='white')
c.create_line(150,200,330,200, width= 2, fill = 'red')
c.create_line(150,350,330,350, width= 2, fill = 'red')
c.create_polygon(50,500,550,500,500,580,100,580,outline='red', width= 2, fill='white')
c.create_arc(120,200,180,350, style = ARC, width = 2, start = 270, extent = 180, outline = 'red')
c.create_arc(300,200,360,350, style = ARC, width = 2, start = 90, extent = 180, outline = 'red')
c.create_oval(460,520,490,550, outline = 'red', width = 2, fill = 'white')
c.create_oval(390,520,420,550, outline = 'red', width = 2, fill = 'white')
for i in range(24):
    c.create_arc(i*25, 590, (i+1)*25, 620, style = ARC, width = 2, start = 15, extent = 150, outline = 'blue')

c.grid(row = 0)

okno.mainloop()