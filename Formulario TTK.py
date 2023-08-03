import tkinter as tk
from tkinter import ttk


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
        self.estiloD.configure("B.TButton", font=("Verdana", 14), padding=(5,0,5,0))
        
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

#---RADIOBUTTON
        self.varOpcion = tk.IntVar()    
        #self.varOpcion.set(0)
        
        self.titulo = ttk.Label(self.framesita,style="Normal.TLabel", text = "Sexo:")
        self.titulo.grid(row=6, column=0,sticky = "e")

        self.opcion1 = ttk.Radiobutton(self.framesita,style="RB.TRadiobutton", text = "Masculino",  variable=self.varOpcion, value = 1)
        self.opcion1.grid(row=6, column=1,sticky = "w")

        self.opcion2 = ttk.Radiobutton(self.framesita,style="RB.TRadiobutton", text = "Femenino", variable=self.varOpcion, value = 2)
        self.opcion2.grid(row=7, column=1,sticky = "w")

#---CHECKBUTTON---
        self.titulo2 = ttk.Label(self.framesita,style="Normal.TLabel", text = "Lenguajes:")
        self.titulo2.grid(row=8, column=0,sticky = "e")
        
        self.python = tk.IntVar()
        self.java = tk.IntVar()
        self.html = tk.IntVar()        
        
        self.checkb1 = ttk.Checkbutton(self.framesita, style="CB.TCheckbutton", text="Python", variable = self.python,onvalue=1, offvalue=0)
        self.checkb1.grid(row=8, column=1,sticky = "w")

        self.checkb2 = ttk.Checkbutton(self.framesita, style="CB.TCheckbutton", text="Java", variable = self.java,onvalue=1, offvalue=0)
        self.checkb2.grid(row=9, column=1,sticky = "w")
        
        self.checkb3 = ttk.Checkbutton(self.framesita, style="CB.TCheckbutton", text="HTML", variable = self.html,onvalue=1, offvalue=0)
        self.checkb3.grid(row=10, column=1,sticky = "w")

#---CUADRO DE TEXTO---
        self.titulo3 = ttk.Label(self.framesita,style="Normal.TLabel", text = "Comentarios:")
        self.titulo3.grid(row=11, column=0,sticky = "e")
        
        self.comentarios = tk.Text(self.framesita, width=22, height=5, font=("Verdana",12))
        self.comentarios.grid(row=11, column=1,sticky = "w", pady=20)

#---BARRA DE NAVEGACION DE CUADRO DE TEXTO---
        self.scrollVert = ttk.Scrollbar(self.framesita, command=self.comentarios.yview)
        self.scrollVert.grid(row=11, column=2, sticky="ns")
        self.comentarios.config(yscrollcommand=self.scrollVert.set)

#---BOTONES---
        for i in range(3): #cantidad de columnas - - -
            self.framesita2.grid_columnconfigure(i, weight=1)
        for j in range(1): #cantidad de filas =
            self.framesita2.grid_rowconfigure(j, weight=1) 
                
        self.botonReiniciar = ttk.Button(self.framesita2, text="Reiniciar",style="B.TButton")
        self.botonReiniciar.grid(row=0, column=0)                                     

        self.botonEnviar = ttk.Button(self.framesita2, text="Enviar",style="B.TButton")
        self.botonEnviar.grid(row=0, column=1)     

        self.botonSalir = ttk.Button(self.framesita2, text="Salir",style="B.TButton")
        self.botonSalir.grid(row=0, column=2)                                     
           


if __name__ == "__main__":
    interfaz = MiInterfaz()
    interfaz.root.mainloop()
