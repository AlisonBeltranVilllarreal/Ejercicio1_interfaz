from tkinter import *
from tkinter import ttk
#import tkinter.ttk as ttk
ventana= Tk()

style= ttk.Style()

style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {"background": "dodger blue", "foreground": "black", "font": ("Arial", 14)},
        "map": {"background": [("selected", "Dodger blue")], "foreground": [("selected", "black")]}
    }
})
style.theme_use("MyStyle")

ventana.geometry("600x450")
ventana.title("Ejercicio_1")

panel = ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

ventana1= ttk.Frame(panel)
panel.add(ventana1, text="      Add     ")

ventana2= ttk.Frame(panel)
panel.add(ventana2, text="      Delete      ")

ventana3= ttk.Frame(panel)
panel.add(ventana3, text="      Search      ")

ventana4= ttk.Frame(panel)
panel.add(ventana4, text="      Services        ")

ventana5= ttk.Frame(panel)
panel.add(ventana5, text="          Help        ")

vacio_Frame=ttk.Frame(ventana1, relief="groove", padding="300 10 300 10")
vacio_Frame.grid(column=0, row=0)

ttk.Label(vacio_Frame, text=" ").grid(column=0, row=0)

datos_Frame=ttk.Frame(ventana1, relief="raised", padding= "5 5 45 5")
datos_Frame.grid(column=0, row=1, sticky=(W))

First=StringVar()
Last=StringVar()
Country=StringVar()

FirstEntry=ttk.Entry(datos_Frame, textvariable=First, font=("Arial", 14), width=12)
FirstEntry.grid(column=1, row=0, pady=10,  sticky=(N))
LastEntry=ttk.Entry(datos_Frame, textvariable=Last, font=("Arial", 14), width=12)
LastEntry.grid(column=3, row=0,  pady=10, sticky=(N))
CountryEntry=ttk.Entry(datos_Frame, textvariable=Country, font=("Arial", 14), width=12)
CountryEntry.grid(column=3, row=3, sticky=(W))

                                                                    #izq arriba der abajo
ttk.Label(datos_Frame, text="First Name: ", font=("Arial", 14),padding="30 10 20 30").grid(column=0, row=0)
ttk.Label(datos_Frame, text="Last Name: ", font=("Arial", 14), padding="20 10 0 30").grid(column=2, row=0)
ttk.Label(datos_Frame, text="Country: ", font=("Arial", 14), padding="0 10 0 0").grid(column=2, row=3)
ttk.Label(datos_Frame, text="Birth Date: ", font=("Arial", 14),padding="30 10 20 0").grid(column=0, row=3)

birt_Frame=ttk.Frame(datos_Frame)
birt_Frame.grid(column=1, row=3)
        
        #entrys de birthday
cumpledi=StringVar()
cumpleMe=StringVar()
cumpleAñ=StringVar()

cumplediEntry= ttk.Entry(birt_Frame, textvariable=cumpledi, width=2, font=("Arial", 14))
cumplediEntry.grid(column=0, row=1, sticky=W)
cumpleMeEntry= ttk.Entry(birt_Frame, textvariable=cumpleMe, width=2, font=("Arial", 14))
cumpleMeEntry.grid(column=2, row=1, padx=6)
cumpleAñEntry= ttk.Entry(birt_Frame, textvariable=cumpleAñ, width=4, font=("Arial", 14))
cumpleAñEntry.grid(column=4, row=1, padx=6)

credit_Frame=ttk.Frame(ventana1, relief="raised", padding= "5 5 86 5")
credit_Frame.grid(column=0, row=4, sticky=(W))

any=StringVar()

anyEntry=ttk.Entry(credit_Frame, textvariable=any, font=("Arial", 14), width=12)
anyEntry.grid(column=1, row=0)
                                                                            #izq arriba der abajo
ttk.Label(credit_Frame, text="Credit Card(if any): ", font=("Arial", 14),padding="30 10 0 0").grid(column=0, row=0,sticky=(W))
ttk.Label(credit_Frame, text="Credit Card Type(if any): ", font=("Arial", 14),padding="30 20 0 0").grid(column=0, row=2,sticky=(W))

ttk.Label(credit_Frame, text="Visa ", font=("Arial", 14),padding="20 20 0 0").grid(column=1, row=2)
ttk.Label(credit_Frame, text="Master Card ", font=("Arial", 14),padding="0 20 0 0").grid(column=4, row=2)

tarjeta=StringVar()
visa= ttk.Radiobutton(credit_Frame,variable=tarjeta, value='visa',padding="25 20 8 0").grid(column=1,row=2,sticky=(W))
master= ttk.Radiobutton(credit_Frame,variable=tarjeta, value='master card',padding="0 20 0 0").grid(column=3,row=2, sticky=(W))

roow_Frame=ttk.Frame(ventana1 ,relief="raised", padding= "5 5 13 5")
roow_Frame.grid(column=0, row=5, sticky=(W))
                                                                #izq arriba der abajo
ttk.Label(roow_Frame, text="ROOW Type: ", font=("Arial", 14),padding="30 10 20 0").grid(column=0, row=0)
ttk.Label(roow_Frame, text="Total Staying Tipe(days): ", font=("Arial", 14),padding="30 10 20 0").grid(column=4, row=0)
        
personita=StringVar()
total=StringVar()

totalEntry=ttk.Entry(roow_Frame, textvariable=total, width=4, font=("Arial", 14))
totalEntry.grid(column=5, row=0)

normal= ttk.Radiobutton(roow_Frame,variable=personita, value='normal').grid(column=1,row= 0, sticky=S)
familiar= ttk.Radiobutton(roow_Frame,variable=personita, value='familiar').grid(column=1,row= 1,sticky=W)
special= ttk.Radiobutton(roow_Frame,variable=personita, value='special').grid(column=1,row=2, sticky=W)

                                                            #izq arriba der abajo
ttk.Label(roow_Frame, text="Normal" , font=("Arial", 14)).grid(column=2, row=0, sticky=S)
ttk.Label(roow_Frame, text="Familiar ", font=("Arial", 14)).grid(column=2, row=1)
ttk.Label(roow_Frame, text="Special ", font=("Arial", 14)).grid(column=2, row=2)

boton_Frame=ttk.Frame(ventana1, relief="raised", padding= " 5 5 5 5 ")
boton_Frame.grid(column=0, row=6)

Button(boton_Frame, text="Submit",font=("Arial", 14)).grid(column=2,row=2,sticky=(W), pady=16, padx=258)

ventana.mainloop()


        

      
