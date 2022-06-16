from tkinter import *
from PIL import ImageTk, Image
ventana =Tk()
ventana.geometry("700x600")

##Icono
ventana.iconbitmap(r'C:\Users\gabri\PycharmProjects\pythonProject\Logo.jpg')
##ImagenDeFondo
# imagen=ImageTk.PhotoImage(Image.open(r'C:\Users\gabri\PycharmProjects\pythonProject\Logo2.jpg').resize((700,600)))
# label=Label(image=imagen)
# label.pack()
def participantes():
    import io
    f = io.open("Lista de equipos", mode="r", encoding="utf-8")
    print("NOMBRE \t\t PAIS \t\t BOMBO \t\t SIGLAS")
    for line in f:
        print(line.split())
    print("\n -------------------------------------------------------")

boton_Listaequipos=Button(ventana, text="Equipos participantes", command=participantes,width=15, height=5)
boton_Listaequipos.grid(row=0, column=0)

def Bombos():
    file = open("Lista de equipos")
    lines = file.readlines()
    lista_equipos = list()
    lista_bombos =[]
    for line in lines:
        equipos = line.split()
        lista_equipos.append(equipos)
        lista_bombos.append(equipos[2])
    Bombo1=[]
    Bombo2 =[]
    Bombo3=[]
    Bombo4=[]
    for i in range(32):
        if(lista_bombos[i]=='1'):
            name=lista_equipos[i]
            Bombo1.append(name[0])
        elif(lista_bombos[i]=='2'):
            name=lista_equipos[i]
            Bombo2.append(name[0])
        elif(lista_bombos[i]=='3'):
            name=lista_equipos[i]
            Bombo3.append(name[0])
        elif (lista_bombos[i] =='4'):
            name=lista_equipos[i]
            Bombo4.append(name[0])

    print("BOMBO 1: \n",Bombo1,"\n--------------------------------------- ","\n \n BOMBO 2: \n", Bombo2,"\n--------------------------------------- ","\n \n BOMBO 3: \n", Bombo3,"\n--------------------------------------- ","\n \n BOMBO 4: \n", Bombo4 ,"\n--------------------------------------- ",)
boton_Bombos=Button(ventana, text="Bombos", command=Bombos, width=15, height=5)
boton_Bombos.grid(row=0, column=1)

def Sorteo():
    file = open("Lista de equipos")
    lines = file.readlines()
    lista_equipos = list()
    lista_bombos = []
    for line in lines:
        equipos = line.split()
        lista_equipos.append(equipos)
        lista_bombos.append(equipos[2])
    Bombo1 = []
    Bombo2 = []
    Bombo3 = []
    Bombo4 = []
    for i in range(32):
        if (lista_bombos[i] == '1'):
            name = lista_equipos[i]
            Bombo1.append(name[0])
        elif (lista_bombos[i] == '2'):
            name = lista_equipos[i]
            Bombo2.append(name[0])
        elif (lista_bombos[i] == '3'):
            name = lista_equipos[i]
            Bombo3.append(name[0])
        elif (lista_bombos[i] == '4'):
            name = lista_equipos[i]
            Bombo4.append(name[0])
    GrupoA=[]
    GrupoB=[]
    GrupoC=[]
    GrupoD=[]
    GrupoE=[]
    GrupoF=[]
    GrupoG=[]
    GrupoH=[]

boton_Sorteo=Button(ventana, text="Sorteo", command=Sorteo, width=15, height=5)
boton_Sorteo.grid(row=0,column=2)
ventana.mainloop()

