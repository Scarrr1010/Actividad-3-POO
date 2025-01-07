
from tkinter import *
from tkinter import messagebox

class Empleado:
    def __init__(self,Codigo,Nombre,NH,VH,PR):
        self.Codigo = Codigo
        self.Nombre = Nombre
        self.NH = NH
        self.VH = VH
        self.PR = PR
    
    def sb(self):
        sb = self.NH*self.VH
        return sb

    def sn(self):
        sb = self.NH*self.VH
        sn = sb - (sb*(self.PR/100))
        return sn

def Interfaz_Empleado():
        codigo = int(Codigo.get())
        nombres = str(Nombres.get())
        nh = float(CantidadHoras.get())
        vh = float(ValorHoras.get())
        pr = float(PorcentajeR.get())
    
        if nh > 0 and vh > 0 and pr > 0:  
            InfoEmpleado = Empleado(codigo,nombres,nh,vh,pr)
            sb = InfoEmpleado.sb()
            sn = InfoEmpleado.sn()
            Resultado.set(f"""Codigo: {InfoEmpleado.Codigo}\nNombre: {InfoEmpleado.Nombre}\nSalario Bruto: {round(InfoEmpleado.sb(),0)}\nSalario Neto: {round(InfoEmpleado.sn(),0)}""")
        else:
             messagebox.showerror("Error", "Por favor, ingresar valores positivos.")


raiz = Tk()
raiz.title("Salario del empleado")
raiz.config(bg="Purple")

Resultado = StringVar()


miFrame = Frame(raiz, width=500, height=400)
miFrame.config(bg="Purple", cursor="pirate")
miFrame.pack()


Codigo = Entry(miFrame)
Codigo.grid(row=1, column=0)
Codigo.config(fg="Black", justify="center")
Nombres = Entry(miFrame)
Nombres.grid(row=3, column=0)
Nombres.config(fg="Black", justify="center")
CantidadHoras = Entry(miFrame)
CantidadHoras.grid(row=5, column=0)
CantidadHoras.config(fg="purple", justify="center")
ValorHoras = Entry(miFrame)
ValorHoras.grid(row=7, column=0)
ValorHoras.config(fg="purple", justify="center")
PorcentajeR = Entry(miFrame)
PorcentajeR.grid(row=9, column=0)
PorcentajeR.config(fg="purple", justify="center")


CodigoLabel = Label(miFrame, text="Ingrese codigo de empleado: ", fg="Black", font=("Comic Sans MS",14))
CodigoLabel.grid(row=0, column=0, padx= 10, pady= 20)
NombresLabel = Label(miFrame, text="Ingrese sus nombres: ", fg="Black", font=("Comic Sans MS",14))
NombresLabel.grid(row=2, column=0, padx= 10, pady= 20)
CantidadHorasLabel = Label(miFrame, text="Ingrese numero de horas trabajadas: ", fg="Black", font=("Comic Sans MS",14))
CantidadHorasLabel.grid(row=4, column=0, padx= 10, pady= 20)
ValorHorasLabel = Label(miFrame, text="Ingrese valor de horas trabajadas: ", fg="Black", font=("Comic Sans MS",14))
ValorHorasLabel.grid(row=6, column=0, padx= 10, pady= 20)
PorcentajeRLabel = Label(miFrame, text="Ingrese porcentaje de retención: ", fg="Black", font=("Comic Sans MS",14))
PorcentajeRLabel.grid(row=8, column=0, padx= 10, pady= 20)


BotonEnvio= Button(raiz, text="Enviar",command=Interfaz_Empleado)
BotonEnvio.pack(pady=20)

ResultadoMostrar = Label(raiz, textvariable=Resultado, justify="left")
ResultadoMostrar.pack(pady=15)

raiz.mainloop()
