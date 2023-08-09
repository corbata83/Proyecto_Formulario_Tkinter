datos = {"Nombre":"", "Apellido":"", "Email":"", "Pais":"", "Edad":"","Cursada":0, "Sexo":"", "Lenguajes":{},
         "Comentarios":""}

import tkinter as tk
from tkinter import ttk
import pandas as pd

class MiInterfaz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Formulario")
        self.root.geometry("400x600")
        self.root.resizable(0,0)

#---ESTILOS---
        self.estiloD = ttk.Style()
        self.estiloD.configure("Titulo.TLabel", font=("Arial", 24), background="#87CEFA")        
        self.estiloD.configure("Normal.TLabel", font=("Verdana", 14), background="#87CEFA", padding=(5,0,5,0))
        self.estiloD.configure("RB.TRadiobutton", font=("Verdana", 14), background="#87CEFA", padding=(5,0,5,0))
        self.estiloD.configure("CB.TCheckbutton", font=("Verdana", 14), background="#87CEFA", padding=(5,0,5,0))
        self.estiloD.configure("SB.TSpinbox", font=("Verdana", 16))
        self.estiloD.configure("scale.TScale", length=300)
        
#---FRAMES---
        self.framesita = ttk.Frame(self.root, style="Normal.TLabel")
        self.framesita.pack(expand=True, fill="both")

        self.framesita2 = ttk.Frame(self.root, style="Normal.TLabel")
        self.framesita2.pack(expand=True, fill="both")
        
#----LABELS----
        self.framesita.grid_columnconfigure(0, weight=1)
        self.framesita.grid_columnconfigure(1, weight=1)                
        self.framesita.grid_columnconfigure(2, weight=1)

        self.titulo = ttk.Label(self.framesita, style="Titulo.TLabel", text="Formulario")
        self.titulo.grid(row=0, column=0, columnspan=3)
               
        self.nombre = ttk.Label(self.framesita,style="Normal.TLabel", text="Nombre:")
        self.nombre.grid(row=1, column=0,sticky = "e") #padx=5, pady=2
        
        self.apellido = ttk.Label(self.framesita, style="Normal.TLabel", text="Apellido:")
        self.apellido.grid(row=2, column=0,sticky = "e")
        
        self.password = ttk.Label(self.framesita, style="Normal.TLabel", text="Password:")
        self.password.grid(row=3, column=0,sticky = "e")
        
        self.mail = ttk.Label(self.framesita, style="Normal.TLabel", text="E-mail:")
        self.mail.grid(row=4, column=0,sticky = "e")
        
        self.pais = ttk.Label(self.framesita, style="Normal.TLabel", text="País:")
        self.pais.grid(row=5, column=0,sticky = "e")
        
#----ENTRYS----        
        self.Enombre = ttk.Entry(self.framesita, font=("Verdana",12), width=18)
        self.Enombre.grid(row=1, column=1,sticky = "w")

        self.Eapellido = ttk.Entry(self.framesita,font=("Verdana", 12), width=18)
        self.Eapellido.grid(row=2, column=1,sticky = "w")
        
        self.Epassword = ttk.Entry(self.framesita, show = "*",font=("Verdana", 12), width=18)
        self.Epassword.grid(row=3, column=1,sticky = "w")
        
        self.Eemail = ttk.Entry(self.framesita,font=("Verdana", 12), width=18)
        self.Eemail.grid(row=4, column=1,sticky = "w")
        
        self.Epais = ttk.Entry(self.framesita,font=("Verdana", 12), width=18)
        self.Epais.grid(row=5, column=1,sticky = "w")

#---SPINBOX EDAD
        self.varNum = tk.IntVar()        

        self.tituloSB = ttk.Label(self.framesita,style="Normal.TLabel", text = "Edad:")
        self.tituloSB.grid(row=6, column=0,sticky = "e")

        self.spinbox = ttk.Spinbox(self.framesita, from_=1, to=100, increment=1,textvariable=self.varNum, style="SB.TSpinbox", width=28)        
        self.spinbox.grid(row=6, column=1, sticky="w")

#---ESCALA PORCENTAJE CURSADA---
        self.varDecimal = tk.DoubleVar()            

        self.escala = ttk.Scale(self.framesita, from_=0, to=100, variable=self.varDecimal, orient=tk.HORIZONTAL,length=187)
        self.escala.grid(row=7, column=1, sticky="w")        

        self.tituloSB = ttk.Label(self.framesita,style="Normal.TLabel", text = str(self.escala.get()))
        self.tituloSB.grid(row=7, column=1,sticky = "e")
        
        self.varDecimal.trace("w", self.update_label)        
        
        self.porcentaje = ttk.Label(self.framesita,style="Normal.TLabel", text = "Cursada:")
        self.porcentaje.grid(row=7, column=0,sticky = "e")     
        
#---RADIOBUTTON SEXO M/F
        self.varOpcion = tk.IntVar()    
        
        self.titulo = ttk.Label(self.framesita,style="Normal.TLabel", text = "Sexo:")
        self.titulo.grid(row=9, column=0,sticky = "e")

        self.opcion1 = ttk.Radiobutton(self.framesita,style="RB.TRadiobutton", text = "Masculino",  variable=self.varOpcion, value = 1)
        self.opcion1.grid(row=9, column=1,sticky = "w")

        self.opcion2 = ttk.Radiobutton(self.framesita,style="RB.TRadiobutton", text = "Femenino", variable=self.varOpcion, value = 2)
        self.opcion2.grid(row=10, column=1,sticky = "w")

#---CHECKBUTTON LENGUAJES---
        self.titulo2 = ttk.Label(self.framesita,style="Normal.TLabel", text = "Lenguajes:")
        self.titulo2.grid(row=11, column=0,sticky = "e")
        
        self.python = tk.IntVar()
        self.java = tk.IntVar()
        self.html = tk.IntVar()        
        
        self.checkb1 = ttk.Checkbutton(self.framesita, style="CB.TCheckbutton", text="Python", variable = self.python,onvalue=1, offvalue=0)
        self.checkb1.grid(row=11, column=1,sticky = "w")

        self.checkb2 = ttk.Checkbutton(self.framesita, style="CB.TCheckbutton", text="Java", variable = self.java,onvalue=1, offvalue=0)
        self.checkb2.grid(row=12, column=1,sticky = "w")
        
        self.checkb3 = ttk.Checkbutton(self.framesita, style="CB.TCheckbutton", text="HTML", variable = self.html,onvalue=1, offvalue=0)
        self.checkb3.grid(row=13, column=1,sticky = "w")

#---CUADRO DE TEXTO---        
        self.titulo3 = ttk.Label(self.framesita,style="Normal.TLabel", text = "Comentarios:")
        self.titulo3.grid(row=14, column=0,sticky = "e")
        
        self.comentarios = tk.Text(self.framesita, width=22, height=5, font=("Verdana",12))
        self.comentarios.grid(row=14, column=1,sticky = "w", pady=20)

#---BARRA DE NAVEGACION DE CUADRO DE TEXTO---
        self.scrollVert = ttk.Scrollbar(self.framesita, command=self.comentarios.yview)
        self.scrollVert.grid(row=14, column=2, sticky="ns", pady=20)
        self.comentarios.config(yscrollcommand=self.scrollVert.set)

#---BOTONES---
        for i in range(3): #cantidad de columnas - - -
            self.framesita2.grid_columnconfigure(i, weight=1)
        for j in range(1): #cantidad de filas =
            self.framesita2.grid_rowconfigure(j, weight=1) 
                
        self.botonReiniciar = tk.Button(self.framesita2, text="Reiniciar", font=("Verdana", 14), width=8, command=self.reiniciar)
        self.botonReiniciar.grid(row=0, column=0)                                     

        self.botonSalir = tk.Button(self.framesita2, text="Salir", font=("Verdana", 14), width=8, bg="red", command=self.salir)
        self.botonSalir.grid(row=0, column=2)                                     

        self.imagen = tk.PhotoImage(file="enviar.png")
        self.botonEnviar = tk.Button(self.framesita2, image=self.imagen, bg="#00FF00", font=("Verdana", 14), height=60,command=self.captura_datos)
        self.botonEnviar.grid(row=0, column=1)     
           
############# FUNCIONES ####################
    def update_label(self, *args):
        self.tituloSB.config(text= round(self.escala.get()))
        
    def captura_datos(self):
        datos["Nombre"] = self.Enombre.get()
        datos["Apellido"] = self.Eapellido.get()
        datos["Email"] = self.Eemail.get()
        datos["Pais"] = self.Epais.get()
        datos["Edad"] = int(self.spinbox.get())
        datos["Cursada"] = round(self.escala.get(), 2)
        datos["Comentarios"] = self.comentarios.get("1.0", "end-1c")
        
        if self.varOpcion.get() == 1:
            datos["Sexo"] = "Masculino"
        elif self.varOpcion.get() == 2:
            datos["Sexo"] = "Femenino"
        
        if self.python.get() == 1:
                datos["Lenguajes"].add("Python")
        elif self.python.get() == 0:
                datos["Lenguajes"].discard("Python")
        if self.java.get() == 1:
                datos["Lenguajes"].add("Java")
        elif self.java.get() == 0:
                datos["Lenguajes"].discard("Java")
        if self.html.get() == 1:
                datos["Lenguajes"].add("HTML")
        elif self.html.get() == 0:
                datos["Lenguajes"].discard("HTML")
               
        self.exportar_a_xls()
        self.reiniciar()
        
    def reiniciar(self):
        self.Enombre.delete(0,"end")
        self.Eapellido.delete(0,"end")
        self.Eemail.delete(0,"end")
        self.Epassword.delete(0,"end")
        self.Epais.delete(0,"end")
        self.spinbox.set("0")
        self.escala.set(0)
        self.comentarios.delete(1.0,"end")
        self.varOpcion.set(None)
        self.python.set(None)
        self.java.set(None)
        self.html.set(None)
    
    def salir(self):
        self.root.destroy()        
            
            
######### EXPORTAR LOS DATOS A XLS ###########
    def exportar_a_xls(self):
        datos_listas = [list(datos.keys()), list(datos.values())]
        df = pd.DataFrame(datos_listas)        
        df_transpuesto = df.transpose()
        archivo_xlsx = "datos_horizontal.xlsx"
        df_transpuesto.to_excel(archivo_xlsx, index=False, header=False)    
                        
if __name__ == "__main__":
    interfaz = MiInterfaz()
    interfaz.root.mainloop()
    

print(datos)