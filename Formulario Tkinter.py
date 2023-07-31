from tkinter import *

class MiInterfaz(Tk):
    def __init__(self):
        super().__init__()
        self.title("Formulario")
        self.geometry("400x400")

        #for i in range(2): #cantidad de filas ≡
        #    self.grid_columnconfigure(i, weight=1)
        #for j in range(7): #cantidad de columnas - - -
        #    self.grid_rowconfigure(j, weight=1)        

#---FRAME---
        self.framesita = Frame(self, bg="orange")
        self.framesita.pack(expand=True, fill = "both")

        self.framesita2 = Frame(self, bg="orange")
        self.framesita2.pack(expand=True, fill = "both")
        
#----LABELS----
        self.framesita.grid_columnconfigure(0, weight=1)
        self.framesita.grid_columnconfigure(1, weight=1)                

        self.titulo = Label(self.framesita,bg="orange", text="Formulario", font=("Verdana", 24))
        self.titulo.grid(row=0, column=0, columnspan=2)
        
        self.nombre = Label(self.framesita,bg="orange", text="Nombre:",font=("Verdana", 14))
        self.nombre.grid(row=1, column=0,sticky = "e", padx=5, pady=2)
        
        self.apellido = Label(self.framesita,bg="orange", text="Apellido:",font=("Verdana", 14))
        self.apellido.grid(row=2, column=0,sticky = "e", padx=5)
        
        self.password = Label(self.framesita,bg="orange", text="Password:",font=("Verdana", 14))
        self.password.grid(row=3, column=0,sticky = "e", padx=5)
        
        self.mail = Label(self.framesita,bg="orange", text="E-mail:",font=("Verdana", 14))
        self.mail.grid(row=4, column=0,sticky = "e", padx=5)
        
        self.pais = Label(self.framesita,bg="orange", text="País:",font=("Verdana", 14))
        self.pais.grid(row=5, column=0,sticky = "e", padx=5)
        
#----ENTRYS----        
        self.Enombre = Entry(self.framesita,font=("Verdana", 14), width=15)
        self.Enombre.grid(row=1, column=1,sticky = "w")

        self.Eapellido = Entry(self.framesita,font=("Verdana", 14), width=15)
        self.Eapellido.grid(row=2, column=1,sticky = "w")
        
        self.Epassword = Entry(self.framesita, show = "*",font=("Verdana", 14), width=15)
        self.Epassword.grid(row=3, column=1,sticky = "w")
        
        self.Eemail = Entry(self.framesita,font=("Verdana", 14), width=15)
        self.Eemail.grid(row=4, column=1,sticky = "w")
        
        self.Epais = Entry(self.framesita,font=("Verdana", 14), width=15)
        self.Epais.grid(row=5, column=1,sticky = "w")

#---RADIOBUTTON
        varOpcion = IntVar()    
        
        self.titulo = Label(self.framesita,bg="orange", text = "Sexo:")
        self.titulo.config(font=("Verdana",14))
        self.titulo.grid(row=6, column=0,sticky = "e", padx=5)

        self.opcion1 = Radiobutton(self.framesita,bg="orange", text = "Masculino",  variable=varOpcion, value = 1)
        self.opcion1.config(font=("Verdana",14))
        self.opcion1.grid(row=6, column=1,sticky = "w")

        self.opcion2 = Radiobutton(self.framesita,bg="orange", text = "Femenino", variable=varOpcion, value = 2)
        self.opcion2.config(font=("Verdana",14))
        self.opcion2.grid(row=7, column=1,sticky = "w")

#---BOTONES---
        #for i in range(3): #cantidad de columnas - - -
        #    self.framesita2.grid_columnconfigure(i, weight=1)
        #for j in range(1): #cantidad de filas =
        #    self.grid_rowconfigure(j, weight=1) 
        
        

        self.botonReiniciar = Button(self.framesita2, text="Reiniciar",font=("Verdana",14))
        self.botonReiniciar.grid(row=0, column=0)                                     

        self.botonEnviar = Button(self.framesita2, text="Enviar",font=("Verdana",14))
        self.botonEnviar.grid(row=0, column=1)     

        self.botonSalir = Button(self.framesita2, text="Salir",font=("Verdana",14))
        self.botonSalir.grid(row=0, column=2)                                     
                                
















if __name__ == "__main__":
    interfaz = MiInterfaz()
    interfaz.mainloop()
