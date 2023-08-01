from tkinter import *

class MiInterfaz(Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulario")
        self.geometry("400x600")
        self.resizable(0,0)
 
#---FRAMES---
        self.framesita = Frame(self, bg="light blue")
        self.framesita.pack(expand=True, fill="both")

        self.framesita2 = Frame(self, bg="light blue")
        self.framesita2.pack(expand=True, fill = "both")
        
#----LABELS----
        self.framesita.grid_columnconfigure(0, weight=1)
        self.framesita.grid_columnconfigure(1, weight=1)                
        self.framesita.grid_columnconfigure(2, weight=1)

        self.titulo = Label(self.framesita,bg="light blue", text="Formulario", font=("Verdana", 24))
        self.titulo.grid(row=0, column=0, columnspan=3)
        
        self.nombre = Label(self.framesita,bg="light blue", text="Nombre:",font=("Verdana", 14))
        self.nombre.grid(row=1, column=0,sticky = "e", padx=5, pady=2)
        
        self.apellido = Label(self.framesita,bg="light blue", text="Apellido:",font=("Verdana", 14))
        self.apellido.grid(row=2, column=0,sticky = "e", padx=5, pady=2)
        
        self.password = Label(self.framesita,bg="light blue", text="Password:",font=("Verdana", 14))
        self.password.grid(row=3, column=0,sticky = "e", padx=5, pady=2)
        
        self.mail = Label(self.framesita,bg="light blue", text="E-mail:",font=("Verdana", 14))
        self.mail.grid(row=4, column=0,sticky = "e", padx=5, pady=2)
        
        self.pais = Label(self.framesita,bg="light blue", text="País:",font=("Verdana", 14))
        self.pais.grid(row=5, column=0,sticky = "e", padx=5, pady=2)
        
#----ENTRYS----        
        self.Enombre = Entry(self.framesita,font=("Verdana", 14), width=18)
        self.Enombre.grid(row=1, column=1,sticky = "w")

        self.Eapellido = Entry(self.framesita,font=("Verdana", 14), width=18)
        self.Eapellido.grid(row=2, column=1,sticky = "w")
        
        self.Epassword = Entry(self.framesita, show = "*",font=("Verdana", 14), width=18)
        self.Epassword.grid(row=3, column=1,sticky = "w")
        
        self.Eemail = Entry(self.framesita,font=("Verdana", 14), width=18)
        self.Eemail.grid(row=4, column=1,sticky = "w")
        
        self.Epais = Entry(self.framesita,font=("Verdana", 14), width=18)
        self.Epais.grid(row=5, column=1,sticky = "w")

#---RADIOBUTTON
        self.varOpcion = IntVar()    
        
        self.titulo = Label(self.framesita,bg="light blue", text = "Sexo:")
        self.titulo.config(font=("Verdana",14))
        self.titulo.grid(row=6, column=0,sticky = "e", padx=5)

        self.opcion1 = Radiobutton(self.framesita,bg="light blue", text = "Masculino",  variable=self.varOpcion, value = 1)
        self.opcion1.config(font=("Verdana",14))
        self.opcion1.grid(row=6, column=1,sticky = "w")

        self.opcion2 = Radiobutton(self.framesita,bg="light blue", text = "Femenino", variable=self.varOpcion, value = 2)
        self.opcion2.config(font=("Verdana",14))
        self.opcion2.grid(row=7, column=1,sticky = "w")

#---CHECKBUTTON---
        self.titulo2 = Label(self.framesita,bg="light blue", text = "Lenguajes:",font=("Verdana",14))
        self.titulo2.grid(row=8, column=0,sticky = "e", padx=5)
        
        self.python = IntVar()
        self.java = IntVar()
        self.html = IntVar()        
        
        self.checkb1 = Checkbutton(self.framesita, text="Python", variable = self.python,onvalue=1, offvalue=0)
        self.checkb1.config(bg="light blue",font=("Verdana",14))
        self.checkb1.grid(row=8, column=1,sticky = "w")

        self.checkb2 = Checkbutton(self.framesita, text="Java", variable = self.java,onvalue=1, offvalue=0)
        self.checkb2.config(bg="light blue",font=("Verdana",14))
        self.checkb2.grid(row=9, column=1,sticky = "w")
        
        self.checkb3 = Checkbutton(self.framesita, text="HTML", variable = self.html,onvalue=1, offvalue=0)
        self.checkb3.config(bg="light blue",font=("Verdana",14))
        self.checkb3.grid(row=10, column=1,sticky = "w")

#---CUADRO DE TEXTO---
        self.titulo3 = Label(self.framesita,bg="light blue", text = "Comentarios:",font=("Verdana",14))
        self.titulo3.grid(row=11, column=0,sticky = "e", padx=5)
        
        self.comentarios = Text(self.framesita, width=18, height=5,font=("Verdana",14))
        self.comentarios.grid(row=11, column=1,sticky = "w")

#---BARRA DE NAVEGACION DE CUADRO DE TEXTO---
        self.scrollVert = Scrollbar(self.framesita, command=self.comentarios.yview)
        self.scrollVert.grid(row=11, column=2, sticky="ns")
        self.comentarios.config(yscrollcommand=self.scrollVert.set)

#---BOTONES---
        for i in range(3): #cantidad de columnas - - -
            self.framesita2.grid_columnconfigure(i, weight=1)
        for j in range(1): #cantidad de filas =
            self.framesita2.grid_rowconfigure(j, weight=1) 
                
        self.botonReiniciar = Button(self.framesita2, text="Reiniciar",font=("Verdana",14))
        self.botonReiniciar.grid(row=0, column=0)                                     

        self.botonEnviar = Button(self.framesita2, text="Enviar",font=("Verdana",14))
        self.botonEnviar.grid(row=0, column=1)     

        self.botonSalir = Button(self.framesita2, text="Salir",font=("Verdana",14))
        self.botonSalir.grid(row=0, column=2)                                     
           


if __name__ == "__main__":
    interfaz = MiInterfaz()
    interfaz.mainloop()
