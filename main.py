from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from estructuras import profesores

ListaProfesores = profesores.ListaProfesores()

class main():
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Menu")
        self.menu.resizable(0,0)
        self.menu.geometry("400x200")
        #self.menu.configure(bg="#18b9e4")
        self.container()

    def container(self):
        self.frame = Frame(height=200,width=400)
        #self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)

        bienvenida = Label(self.frame , text="¡Bievenido al control de asistencia!")
        bienvenida.pack
        bienvenida.place(x=10,y=10)
        bienvenida.config(font=("Consolas",13))

        #Botonoes
        botonCarga =  Button(self.frame,bg="#5ed1fa",font=("Consolas",12),text="Iniciar sesion", command=self.ingresar)
        botonCarga.place(x=95,y=50)



        botonSalir = Button(self.frame,bg="#5ed1fa",font=("Consolas",12), text="Salir",command=self.menu.destroy)
        botonSalir.place(x=128,y=95)

        self.frame.mainloop()
    
    def ingresar(self):
        self.menu.destroy()
        Ingresar()

class Ingresar():
    def __init__(self):
        self.ingreso = Tk()
        self.ingreso.title("Iniciar sesión")
        self.ingreso.resizable(0, 0)
        self.ingreso.geometry("400x250")
        self.container()

    def container(self):
        self.frame = Frame(height=250, width=400)
        self.frame.pack(padx=25, pady=25)

        # Labels
        usuario_label = Label(self.frame, text="Usuario:")
        usuario_label.place(x=10, y=10)
        usuario_label.config(font=("Consolas", 13))

        contrasena_label = Label(self.frame, text="Contraseña:")
        contrasena_label.place(x=10, y=50)
        contrasena_label.config(font=("Consolas", 13))

        # Entry fields
        self.usuario_entry = Entry(self.frame, font=("Consolas", 12))
        self.usuario_entry.place(x=150, y=10)

        self.contrasena_entry = Entry(self.frame, font=("Consolas", 12), show="*")
        self.contrasena_entry.place(x=150, y=50)

        # Botones
        botonCarga = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Iniciar sesión", command=self.sesion)
        botonCarga.place(x=115, y=100)

        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Regresar", command=self.regresar)
        botonSalir.place(x=128, y=145)

        self.frame.mainloop()

    def regresar(self):
        self.ingreso.destroy()
        print("Regresar al menú principal")

    def sesion(self):
        # Obtener los valores de los campos de texto al presionar el botón
        usuario = self.usuario_entry.get()
        contrasenia = self.contrasena_entry.get()

        # Validar si el usuario es admin y la contraseña es admin
        if usuario == "":
            messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos")
            self.usuario_entry.delete(0, END)
            self.contrasena_entry.delete(0, END)
        elif contrasenia == "":
            messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos")
            self.usuario_entry.delete(0, END)
            self.contrasena_entry.delete(0, END)
        elif usuario == "" and contrasenia == "":
            messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos")
            self.usuario_entry.delete(0, END)
            self.contrasena_entry.delete(0, END)
        elif usuario == "admin" and contrasenia == "admin":
            print("¡Bienvenido al modo administrador!")
            self.ingreso.destroy()
            Admin()
        else:
            print(f"Usuario: {usuario} | Contraseña: {contrasenia}")
            messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos")
            self.usuario_entry.delete(0, END)
            self.contrasena_entry.delete(0, END)
    
class Registrarme():
    def __init__(self):
        print("hola")


class Admin():
    def __init__(self):
        self.admin = Tk()
        self.admin.title("Administrador")
        self.admin.resizable(0,0)
        self.admin.geometry("400x250")
        self.container()

    def container(self):
        self.frame = Frame(height=250, width=400)
        self.frame.pack(padx=25, pady=25)

        # Labels
        usuario_label = Label(self.frame, text="Bievenido al modo administrador")
        usuario_label.pack
        usuario_label.place(x=10, y=10)
        usuario_label.config(font=("Consolas", 13))


        # Buttons
        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Registrar profesor",command=self.registrar)
        botonSalir.place(x=90, y=50)

        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Ver profesores")
        botonSalir.place(x=110, y=100)

        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Regresar", command=self.regresar)
        botonSalir.place(x=130, y=150)

        self.frame.mainloop()
        
    def regresar(self):
        self.admin.destroy()
        main()
    
    def registrar(self):
        self.admin.destroy()
        agregar()

class agregar():
    def __init__(self): 
        
        self.agregar = Tk()
        self.agregar.title("Registrar Profesor")
        self.agregar.resizable(0, 0)
        self.agregar.geometry("400x300")
        self.container()

    def container(self):
        self.frame = Frame(height=300, width=400)
        self.frame.pack(padx=25, pady=25)

        # Labels
        nombre_label = Label(self.frame, text="Nombre:")
        nombre_label.place(x=10, y=10)
        nombre_label.config(font=("Consolas", 13))

        password_label = Label(self.frame, text="Password:")
        password_label.place(x=10, y=50)
        password_label.config(font=("Consolas", 13))

        password_label = Label(self.frame, text="Confirmar:")
        password_label.place(x=10, y=90)
        password_label.config(font=("Consolas", 13))


        # Entry fields
        self.nombre_entry = Entry(self.frame, font=("Consolas", 12))
        self.nombre_entry.place(x=150, y=10)

        self.password_entry = Entry(self.frame, font=("Consolas", 12),show="*")
        self.password_entry.place(x=150, y=50)

        self.password_confir_entry = Entry(self.frame, font=("Consolas", 12),show="*")
        self.password_confir_entry.place(x=150, y=90)

        # Buttons
        botonRegistrar = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Registrar", command=self.registrar)
        botonRegistrar.place(x=130, y=140)

        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Regresar", command=self.regresar)
        botonSalir.place(x=134, y=190)

        self.frame.mainloop()

    def registrar(self):
        nombre = self.nombre_entry.get()
        password = self.password_entry.get()
        confirmar = self.password_confir_entry.get()

        if nombre and password and confirmar:
            if password != confirmar:
                messagebox.showerror("Error de registro", "Las contraseñas no coinciden")
                self.password_entry.delete(0, END)
                self.password_confir_entry.delete(0, END)
                return
            ListaProfesores.agregar_profesor(nombre, password)
            messagebox.showinfo("Registro exitoso", "Profesor registrado correctamente")
            self.nombre_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.id_entry.delete(0, END)
            ListaProfesores.mostrar_profesores()
        else:
            messagebox.showerror("Error de registro", "Todos los campos son obligatorios")

    def regresar(self):
        self.agregar.destroy()
        Admin()
        
        

        

# INICIAR EL MAIN DEL PROGRAMA
if __name__ == '__main__':
    agregar()
    