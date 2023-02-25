from Omamodule import*
from tkinter import*
from tkinter import ttk


def calculate_name_value(event):
    """
    :param str nimi: Nimi
    :param file tabel.txt: nime arvede fail 
    :rtype: int nime number
    """
    nimi=ent.get()
    with open('tabel.txt', 'r') as f:
        nimi_arved = {}
        for line in f:
            täht, number = line.strip().split(',')
            nimi_arved[täht] = int(number)

    nimi_arv = 0
    for täht in nimi.lower():
        if täht in nimi_arved:
            nimi_arv += nimi_arved[täht]

    while nimi_arv > 9:
        uus_arv = 0
        for digit in str(nimi_arv):
            uus_arv += int(digit)
        nimi_arv = uus_arv
    answ1.configure(text=nimi_arv)

def nimi_arvestus(event):
    number=answ1.cget("text")
    number=str(number)
    with open('Nime_väärtused.txt', 'r') as f:
        file_contents = f.read()
    lines = file_contents.splitlines()
    for line in lines:
        if number in line:
            t = line[line.index(number)+1:].strip()
            te= t.replace("^", "\n")
            answ2.configure(text=te)
            return
        else:
            answ2.configure(text='Нет значения')

aken=Tk()
aken.title("Numegoloogia Nime arv")
aken.geometry("750x550")

head=Label(aken,
          text="Numegoloogia Nime arv",
          font="Arial 40",
          bg="#F0F8FF",
          fg="Black"
          )

text1=Label(aken,
          text="Введите имя",
          font="Arial 20",
          bg="#F0F8FF",
          fg="Black"
          )

answ1=Label(aken,
             text="",
             font="Arial 15",
             bg="#F0F8FF",
             width=20,
             height=2
             )

answ2=Label(aken,
             text="",
             font="Arial 15",
             bg="#F0FFF0",
             width=70,
             height=10
             )

ent=Entry(aken,
          text="",
          fg="black", 
          bg="#F0FFFF",
          width=20,
          font="Arial 25",
          )

btn1=Button(aken, 
           text="Узнать\nзначение\nчисла", 
           font="Arial 20", 
           fg="black", 
           bg="#F0FFFF", 
           width=15, 
           height=3,
           relief=RAISED)# SUNKEN, GROOVE


head.grid(row=0,column=0)

text1.grid(row=1,column=0)

ent.grid(row=2,column=0)

answ1.grid(row=4,column=0)

btn1.grid(row=5,column=0)

answ2.grid(row=6,column=0)

ent.bind("<Return>",calculate_name_value)
btn1.bind("<Button-1>",nimi_arvestus)

aken.mainloop()