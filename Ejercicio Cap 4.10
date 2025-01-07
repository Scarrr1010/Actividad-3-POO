
from tkinter import *
from tkinter import messagebox

class MatriculaE:
    def __init__(self,NI,Nombre,Patrimonio,Estrato):
        self.NI = NI
        self.Nombre = Nombre
        self.Patrimonio = Patrimonio
        self.Estrato = Estrato
    
    def Matricula(self):
        Matricula = 50000
        if self.Patrimonio  > 2000000 and self.Estrato > 3:
             return Matricula + (self.Patrimonio*0.03)
        else:
             return Matricula


def Interfaz_Matricula():
        NI = int(NumeroI.get())
        nombre = str(Nombres.get())
        Patrimonio = float(patrimonio.get())
        Estrato = int(estrato.get())
        if Patrimonio > 0 and Estrato >= 0:
            InfoEstudiante = MatriculaE(NI,nombre,Patrimonio,Estrato)
            matricula = InfoEstudiante.Matricula()
            Resultado.set(f"""Numero de inscripción: {NI}\nNombre: {nombre}\nPago por matricula: {round(matricula,0)}""")
        else:
             messagebox.showerror("Error", "Por favor, ingresar valores positivos.")


raiz = Tk()
raiz.title("Precio Matricula")
raiz.config(bg="Purple")

Resultado = StringVar()


miFrame = Frame(raiz, width=500, height=400)
miFrame.config(bg="Purple", cursor="pirate")
miFrame.pack()


NumeroI = Entry(miFrame)
NumeroI.grid(row=1, column=0, pady=10)
NumeroI.config(fg="Black", justify="center")
Nombres = Entry(miFrame)
Nombres.grid(row=3, column=0, pady=10)
Nombres.config(fg="Black", justify="center")
patrimonio = Entry(miFrame)
patrimonio.grid(row=5, column=0, pady=10)
patrimonio.config(fg="purple", justify="center")
estrato = Entry(miFrame)
estrato.grid(row=7, column=0, pady=10)
estrato.config(fg="purple", justify="center")


NumeroILabel = Label(miFrame, text="Ingrese numero de inscripción: ", fg="Black", font=("Comic Sans MS",14))
NumeroILabel.grid(row=0, column=0, padx= 10, pady= 10)
NombreLabel = Label(miFrame, text="Ingrese su nombre: ", fg="Black", font=("Comic Sans MS",14))
NombreLabel.grid(row=2, column=0, padx= 10, pady= 10)
PatrimonioLabel = Label(miFrame, text="Ingrese su patrimonio: ", fg="Black", font=("Comic Sans MS",14))
PatrimonioLabel.grid(row=4, column=0, padx= 10, pady= 10)
EstratoLabel = Label(miFrame, text="Ingrese su estrato: ", fg="Black", font=("Comic Sans MS",14))
EstratoLabel.grid(row=6, column=0, padx= 10, pady= 10)


BotonEnvio= Button(raiz, text="Enviar",command=Interfaz_Matricula)
BotonEnvio.pack(pady=10)


ResultadoMostrar = Label(raiz, textvariable=Resultado, justify="left")
ResultadoMostrar.pack(pady=10)

raiz.mainloop()

