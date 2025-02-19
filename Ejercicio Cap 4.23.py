from tkinter import *
from tkinter import messagebox
import math

class Solucionescuadraticas:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def solucion1(self):
        if (math.pow(self.B,2)) - 4*(self.A)*(self.C) > 0:
             X1 = -(self.B) + math.sqrt((math.pow(self.B,2)) - 4*(self.A)*(self.C))
             return X1
    def solucion2(self):
        if (math.pow(self.B,2)) - 4*(self.A)*(self.C) > 0:
             X2 = -(self.B) - math.sqrt((math.pow(self.B,2)) - 4*(self.A)*(self.C))
             return X2    


def Interfaz_Soluciones():
        a = float(NumeroA.get())
        b = float(NumeroB.get())
        c = float(NumeroC.get())
        Valores = Solucionescuadraticas(a,b,c)
        if Valores.solucion1() != None:  
            S1 = Valores.solucion1()
            S2 = Valores.solucion2()
            Resultado.set(f"""La ecuación cuadrática {a}x^2+{b}x+{c} tiene como soluciones: X={S1} y X={S2}""")
        else:
             messagebox.showinfo("Información", f"La ecuación cuadrática ({a}x^2)+({b}x)+({c}), no tiene solución en los reales.")


raiz = Tk()
raiz.title("Solución Ecuación Cuadrática Ax^2+Bx+C")
raiz.config(bg="Purple")

Resultado = StringVar()

miFrame = Frame(raiz, width=500, height=400)
miFrame.config(bg="Purple", cursor="pirate")
miFrame.pack()


NumeroA = Entry(miFrame)
NumeroA.grid(row=1, column=0, pady=10)
NumeroA.config(fg="Black", justify="center")
NumeroB = Entry(miFrame)
NumeroB.grid(row=3, column=0, pady=10)
NumeroB.config(fg="Black", justify="center")
NumeroC = Entry(miFrame)
NumeroC.grid(row=5, column=0, pady=10)
NumeroC.config(fg="Black", justify="center")


NumeroALabel = Label(miFrame, text="Ingrese la constante A: ", fg="Black", font=("Comic Sans MS",14))
NumeroALabel.grid(row=0, column=0, padx= 10, pady= 10)
NumeroBLabel = Label(miFrame, text="Ingrese la constante B: ", fg="Black", font=("Comic Sans MS",14))
NumeroBLabel.grid(row=2, column=0, padx= 10, pady= 10)
NumeroCLabel = Label(miFrame, text="Ingrese la constante C: ", fg="Black", font=("Comic Sans MS",14))
NumeroCLabel.grid(row=4, column=0, padx= 10, pady= 10)

BotonEnvio= Button(raiz, text="Enviar",command=Interfaz_Soluciones)
BotonEnvio.pack(pady=10)


ResultadoMostrar = Label(raiz, textvariable=Resultado, justify="left")
ResultadoMostrar.pack(pady=10)


raiz.mainloop()
