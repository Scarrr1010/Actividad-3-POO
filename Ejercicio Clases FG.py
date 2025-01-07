

import math
from tkinter import *
from tkinter import messagebox

class Figuras:
    def __init__(self, figura):
        self.figura = figura

    def area(self):
        pass

    def perimetro(self):
        pass

class Cuadrado(Figuras):
    def __init__(self,lado):
        self.Lado = lado
    def areaCu(self):
        area = math.pow(self.Lado,2)
        return area
    def periCu(self):
        perimetro = self.Lado*4
        return perimetro

class Rectangulo(Figuras):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def areaRec(self):
        area = (self.base)*(self.altura)
        return area
    def periRec(self):
        perimetro = 2*(self.base) + 2*(self.altura)
        return perimetro

class Circulo(Figuras):
    def __init__(self,radio):
        self.radio = radio
    def areaCir(self):
        area = (math.pi)*(math.pow(self.radio,2))
        return area
    def periCir(self):
        perimetro = 2*(math.pi)*(self.radio)
        return perimetro

class Triangulo(Figuras):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def areaTri(self):
        area = ((self.base)*(self.altura))/2
        return area
    def periTri(self):
        perimetro = (self.base) + (self.altura) + self.hipo()
        return perimetro
    def hipo(self):
        hipotenusa = math.sqrt((math.pow(self.base,2))+(math.pow(self.altura,2)))
        return hipotenusa
    def TipoTri(self):
        if self.base == self.altura and self.base == self.hipo():
            return "Equilatero"
        elif self.base != self.altura and self.base != self.hipo():
            return "Escaleno"
        else:
            return "Isosceles"
    

def Interfaz_cuadrado():
        lado = float(ladoCU.get())
        cuadrado = Cuadrado(lado)
        area = cuadrado.areaCu()
        perimetro = cuadrado.periCu()
        if lado > 0:
            messagebox.showinfo("Información del cuadrado", f"Área: {area}\nPerímetro: {perimetro}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa un valor positivo.")


def Interfaz_rectangulo():
        base = float(BaseRec.get())
        altura = float(AlturaRec.get())
        rectangulo = Rectangulo(base, altura)
        area = rectangulo.areaRec()
        perimetro = rectangulo.periRec()
        if base > 0 and altura > 0:
            messagebox.showinfo("Información del rectángulo", f"Área: {area}\nPerímetro: {perimetro}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa valores positivos.")


def Interfaz_circulo():
        radio = float(RadioCir.get())
        circulo = Circulo(radio)
        area = circulo.areaCir()
        perimetro = circulo.periCir()
        if radio > 0:
            messagebox.showinfo("Información del círculo", f"Área: {area}\nPerímetro: {perimetro}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa un valor positivo.")


def Interfaz_triangulo():
        base = float(BaseTri.get())
        altura = float(AlturaTri.get())
        triangulo = Triangulo(base, altura)
        area = triangulo.areaTri()
        perimetro = triangulo.periTri()
        tipo = triangulo.TipoTri()
        if base > 0 and altura > 0:
             messagebox.showinfo("Información del triángulo",f"Área: {area}\nPerímetro: {perimetro}\nTipo: {tipo}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa valores positivos.")

def VentanaOpciones(seleccion):
    for widget in miFrame.winfo_children():
        widget.pack_forget()

    figura = FS.get()

    if figura == "Cuadrado":
        Label(miFrame, text="Lado:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        ladoCU.pack()
        Button(miFrame, text="Calcular Datos", command=Interfaz_cuadrado).pack(pady=20)

    elif figura == "Rectángulo":
        Label(miFrame, text="Base:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        BaseRec.pack()
        Label(miFrame, text="Altura:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        AlturaRec.pack()
        Button(miFrame, text="Calcular Datos", command=Interfaz_rectangulo).pack(pady=20)

    elif figura == "Círculo":
        Label(miFrame, text="Radio:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        RadioCir.pack()
        Button(miFrame, text="Calcular Datos", command=Interfaz_circulo).pack(pady=20)

    elif figura == "Triángulo":
        Label(miFrame, text="Base:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        BaseTri.pack()
        Label(miFrame, text="Altura:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        AlturaTri.pack()
        Button(miFrame, text="Calcular Datos", command=Interfaz_triangulo).pack(pady=15)


raiz = Tk()
raiz.title("Datos Figuras Geométricas")
raiz.config(bg="Purple")


FS = StringVar()
FS.set("Selecciona una figura")

PreguntaLabel = Label(raiz, text="¿Qué figura desea analizar?:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
MenuF = OptionMenu(raiz, FS, "Cuadrado", "Rectángulo", "Círculo", "Triángulo", command=VentanaOpciones)
MenuF.pack(pady=10)


miFrame = Frame(raiz)
miFrame.config(bg="Purple", cursor="pirate")
miFrame.pack(pady=10)


ladoCU = Entry(miFrame)
ladoCU.config(fg="Black", justify="center")
BaseRec = Entry(miFrame)
BaseRec.config(fg="Black", justify="center")
AlturaRec = Entry(miFrame)
AlturaRec.config(fg="Black", justify="center")
RadioCir = Entry(miFrame)
RadioCir.config(fg="Black", justify="center")
BaseTri = Entry(miFrame)
BaseTri.config(fg="Black", justify="center")
AlturaTri = Entry(miFrame)
AlturaTri.config(fg="Black", justify="center")


raiz.mainloop()
