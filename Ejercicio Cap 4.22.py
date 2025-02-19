
from tkinter import *
from tkinter import messagebox

class Salarios:
    def __init__(self,Nombre,VH,NHM):
        self.Nombre = Nombre
        self.VH = VH
        self.NHM = NHM
    
    def SM(self):
        return self.VH*self.NHM
        


def Interfaz_SalariosM():
        nombre = str(Nombres.get())
        VH = float(vh.get())
        NHM = int(nhm.get())
        if VH > 0 and NHM > 0:
            InfoEstudiante = Salarios(nombre,VH,NHM)
            Salario = InfoEstudiante.SM()
            if Salario > 450000:
                Resultado.set(f"""Nombre: {nombre}\nSalario: {Salario}""")
            else:
                Resultado.set(f"""Nombre: {nombre}""")
        else:
             messagebox.showerror("Error", "Por favor, ingresar valores positivos.")


raiz = Tk()
raiz.title("Precio Matricula")
raiz.config(bg="Purple")

Resultado = StringVar()


miFrame = Frame(raiz, width=500, height=400)
miFrame.config(bg="Purple", cursor="pirate")
miFrame.pack()


Nombres = Entry(miFrame)
Nombres.grid(row=1, column=0, pady=10)
Nombres.config(fg="Black", justify="center")
vh = Entry(miFrame)
vh.grid(row=3, column=0, pady=10)
vh.config(fg="purple", justify="center")
nhm = Entry(miFrame)
nhm.grid(row=5, column=0, pady=10)
nhm.config(fg="purple", justify="center")


NombreLabel = Label(miFrame, text="Ingrese su nombre: ", fg="Black", font=("Comic Sans MS",14))
NombreLabel.grid(row=0, column=0, padx= 10, pady= 10)
vhLabel = Label(miFrame, text="Ingrese salario por hora: ", fg="Black", font=("Comic Sans MS",14))
vhLabel.grid(row=2, column=0, padx= 10, pady= 10)
nhmLabel = Label(miFrame, text="Ingrese numero de horas trabajadas al mes: ", fg="Black", font=("Comic Sans MS",14))
nhmLabel.grid(row=4, column=0, padx= 10, pady= 10)


BotonEnvio= Button(raiz, text="Enviar",command=Interfaz_SalariosM)
BotonEnvio.pack(pady=10)


ResultadoMostrar = Label(raiz, textvariable=Resultado, justify="left")
ResultadoMostrar.pack(pady=10)

raiz.mainloop()
