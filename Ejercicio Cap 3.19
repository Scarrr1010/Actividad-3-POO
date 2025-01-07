
from tkinter import *
from tkinter import messagebox
import math

class Triangulo:
    def __init__(self,LadoA):
        self.LadoA = LadoA
    def Perimetro(self):
        Perimetro = self.LadoA*3
        return Perimetro
    def altura(self):
        altura = math.sqrt((math.pow(self.LadoA,2) - math.pow((self.LadoA/2),2)))
        return altura
    def area(self):
        altura = math.sqrt((math.pow(self.LadoA,2) - math.pow((self.LadoA/2),2)))
        area = (self.LadoA*altura)/2
        return area

def Interfaz_Triangulo():
        TamañoLado = float(TrianguloLado.get())
        if TamañoLado > 0:  
            InfoIngresada = Triangulo(TamañoLado)
            perimetro = InfoIngresada.Perimetro()
            altura = InfoIngresada.altura()
            area = InfoIngresada.area()
            Resultado.set(f"Perímetro: {round(perimetro,2)}\nAltura: {round(altura,2)}\nÁrea: {round(area,2)}")
        else:
             messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido para el lado.")


raiz = Tk()
raiz.title("Datos de triangulo")
raiz.config(bg="Purple")

Resultado = StringVar()


miFrame = Frame(raiz, width=500, height=400)
miFrame.config(bg="Purple", cursor="pirate")
miFrame.pack()


LadoLabel = Label(miFrame, text="Ingrese lado A del Triangulo (Equilatero): ", fg="Black", font=("Comic Sans MS",14))
LadoLabel.grid(padx= 10, pady= 10)


TrianguloLado = Entry(miFrame)
TrianguloLado.grid(pady=10)
TrianguloLado.config(fg="Black", justify="center")



BotonEnvio= Button(raiz, text="Enviar",command=Interfaz_Triangulo)
BotonEnvio.pack(pady=10)


ResultadoMostrar = Label(raiz, textvariable=Resultado, justify="left")
ResultadoMostrar.pack(pady=10)


raiz.mainloop()
