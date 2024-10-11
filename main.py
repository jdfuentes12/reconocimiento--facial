from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from estructuras import profesores
import cv2
import os
import imutils


ListaProfesores = profesores.ListaProfesores()

class main():
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Menu")
        self.menu.resizable(0,0)
        self.menu.geometry("400x200")
        #ListaProfesores.agregar_profesor("jose","123")
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
        password = self.contrasena_entry.get()

        loginProfesor = ListaProfesores.buscar_nombre_password(usuario, password)
        # Validar si el usuario es admin y la contraseña es admin
        if usuario == "":
            messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos")
            self.usuario_entry.delete(0, END)
            self.contrasena_entry.delete(0, END)
        elif password == "":
            messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos")
            self.usuario_entry.delete(0, END)
            self.contrasena_entry.delete(0, END)
        elif usuario == "" and password == "":
            messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos")
            self.usuario_entry.delete(0, END)
            self.contrasena_entry.delete(0, END)
        elif loginProfesor != None:
            self.ingreso.destroy()
            Profesor(loginProfesor)

            
        elif usuario == "admin" and password == "admin":
            print("¡Bienvenido al modo administrador!")
            self.ingreso.destroy()
            Admin()
        else:
            print(f"Usuario: {usuario} | Contraseña: {password}")
            messagebox.showerror("Error de autenticación", "Usuario o contraseña incorrectos")
            self.usuario_entry.delete(0, END)
            self.contrasena_entry.delete(0, END)    

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

        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Ver profesores", command= self.ver_profesores)
        botonSalir.place(x=110, y=100)

        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Regresar", command=self.regresar)
        botonSalir.place(x=130, y=150)

        self.frame.mainloop()
        
    def regresar(self):
        self.admin.destroy()
        main()
    
    def registrar(self):
        self.admin.destroy()
        agregar_Profesor()
    
    def ver_profesores(self):
        self.admin.destroy()
        ver_profesores()

class agregar_Profesor():
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

        password_label = Label(self.frame, text="Usuario:")
        password_label.place(x=10, y=50)
        password_label.config(font=("Consolas", 13))

        password_label = Label(self.frame, text="Password:")
        password_label.place(x=10, y=90)
        password_label.config(font=("Consolas", 13))

        # Entry fields
        self.nombre = Entry(self.frame, font=("Consolas", 12))
        self.nombre.place(x=150, y=10)

        self.usuario = Entry(self.frame, font=("Consolas", 12))
        self.usuario.place(x=150, y=50)

        self.password = Entry(self.frame, font=("Consolas", 12),show="*")
        self.password.place(x=150, y=90)

        # Buttons
        botonRegistrar = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Registrar", command=self.registrar)
        botonRegistrar.place(x=130, y=140)

        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Regresar", command=self.regresar)
        botonSalir.place(x=134, y=190)

        self.frame.mainloop()

    def registrar(self):
        nombre = self.nombre.get()
        usuario = self.usuario.get()
        password = self.password.get()

        if nombre and usuario and password:
            ListaProfesores.agregar_profesor(nombre, password,usuario)
            messagebox.showinfo("Registro exitoso", "Profesor registrado correctamente")
            self.nombre.delete(0, END)
            self.usuario.delete(0, END)
            self.password.delete(0, END)
            ListaProfesores.mostrar_profesores()
        else:
            messagebox.showerror("Error de registro", "Todos los campos son obligatorios")

    def regresar(self):
        self.agregar.destroy()
        Admin()
        
class ver_profesores():
    def __init__(self):
        self.ver_profesores = Tk()
        self.ver_profesores.title("Lista de Profesores")
        self.ver_profesores.resizable(0, 0)
        self.ver_profesores.geometry("700x350")
        self.container()

    def container(self):
        self.frame = Frame(height=350, width=700)
        self.frame.pack(padx=25, pady=25)

        # Treeview
        self.tree = ttk.Treeview(self.frame, columns=("Nombre","Usuario", "Password"), show='headings')
        self.tree.heading("Nombre",text="Nombre")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.heading("Password", text="Password")
        self.tree.pack(fill=BOTH, expand=True)

        # Botón de regresar
        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Regresar", command=self.regresar)
        botonSalir.pack(pady=10)

        # Insertar datos en la tabla
        tamanio = ListaProfesores.tamanio()

        if tamanio == 0:
            messagebox.showerror("Advertencia", "No hay profesores registrados")
        else: 
            for i in range(1, tamanio + 1):
                profesor = ListaProfesores.buscar_profesor(i)
                self.tree.insert("", "end", values=(profesor.nombre,profesor.usuario, profesor.password))
        
        # Centrar el contenido de la lista
        self.tree.column("Nombre", anchor=CENTER)
        self.tree.column("Usuario", anchor=CENTER)
        self.tree.column("Password", anchor=CENTER)

        self.frame.mainloop()

    def regresar(self):
        self.ver_profesores.destroy()
        Admin()

class Profesor():
    def __init__(self,nodo_Profesor):
        self.profesor = Tk()
        self.profesor.title("Profesor")
        self.profesor.resizable(0, 0)
        self.profesor.geometry("400x300")
        self.container(nodo_Profesor)   

    def container(self,nodo_Profesor):
        self.frame = Frame(height=300, width=400)
        self.frame.pack(padx=25, pady=25)
        nombre = nodo_Profesor.nombre
        self.nodoprofesor = nodo_Profesor
        # Labels
        bienvenida_label = Label(self.frame, text=("Bievenido " ))
        bienvenida_label.place(x=10, y=10)
        bienvenida_label.config(font=("Consolas", 13))
        
        bienvenida_label = Label(self.frame, text=(nombre))
        bienvenida_label.place(x=100, y=10)
        bienvenida_label.config(font=("Consolas", 13))

        # Buttons
        botonAgregar = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Registrar estudiante",command=self.registrarEstudiantes)
        botonAgregar.place(x=90, y=50)

        botonVer = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Ver estudiantes",command=self.verEstudiantes)
        botonVer.place(x=110, y=100)

        botonAsistencia = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Asistencia")
        botonAsistencia.place(x=130, y=150)

        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Regresar", command=self.regresar)
        botonSalir.place(x=140, y=200)

        self.frame.mainloop()

    def regresar(self):
        self.profesor.destroy()
        main()
    
    def registrarEstudiantes(self):
        self.profesor.destroy()
        Registrar_Estudiante(self.nodoprofesor)
    
    def verEstudiantes(self):
        self.profesor.destroy()
        Ver_Estudiantes(self.nodoprofesor)

class Registrar_Estudiante:
    def __init__(self,nodoProfesor):
        self.registrar_estudiante = Tk()
        self.registrar_estudiante.title("Registrar Estudiante")
        self.registrar_estudiante.resizable(0, 0)
        self.registrar_estudiante.geometry("400x300")
        self.nodoProfesor = nodoProfesor
        print(nodoProfesor.nombre)
        self.container()

    def container(self):
        self.frame = Frame(height=300, width=400)
        self.frame.pack(padx=25, pady=25)

        # Labels
        nombre_label = Label(self.frame, text="Nombre:")
        nombre_label.place(x=10, y=10)
        nombre_label.config(font=("Consolas", 13))

        matricula_label = Label(self.frame, text="Carné:")
        matricula_label.place(x=10, y=50)
        matricula_label.config(font=("Consolas", 13))

        # Entry fields
        self.nombre_entry = Entry(self.frame, font=("Consolas", 12))
        self.nombre_entry.place(x=150, y=10)

        self.carne_entry = Entry(self.frame, font=("Consolas", 12))
        self.carne_entry.place(x=150, y=50)

        # Buttons
        botonRegistrar = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Registrar", command=self.registrar)
        botonRegistrar.place(x=130, y=100)

        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Regresar", command=self.regresar)
        botonSalir.place(x=134, y=150)

        self.frame.mainloop()

    def registrar(self):
        nombre = self.nombre_entry.get()
        carne = self.carne_entry.get()

        if nombre and carne:
            # Aquí deberías agregar el código para registrar al estudiante
            self.nodoProfesor.estudiantes.insertar_estudiante(nombre,carne)
            self.nodoProfesor.estudiantes.mostrar_estudiantes()
            nombreProfesor = self.nodoProfesor.nombre
            dataPath = 'c:/Users/jose2/OneDrive/Documentos/reconocimiento--facial/faces' #Cambia a la ruta donde hayas almacenado Data
            datapath1 = dataPath + '/' + nombreProfesor

            datapath2 = datapath1 + '/' + nombre

            if not os.path.exists(datapath2):
                print('Carpeta creada: ',datapath2)
                os.makedirs(datapath2)
            cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
            faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
            count = 0

            while True:
                ret, frame = cap.read()
                if ret == False: break
                frame =  imutils.resize(frame, width=640)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                auxFrame = frame.copy()
                faces = faceClassif.detectMultiScale(gray,1.3,5)

                for (x,y,w,h) in faces:
                    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    rostro = auxFrame[y:y+h,x:x+w]
                    rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(datapath2 + '/rotro_{}.jpg'.format(count),rostro)
                    count = count + 1
                cv2.imshow('frame',frame)

                k =  cv2.waitKey(1)
                if k == 27 or count >= 100:
                    break

            cap.release()
            cv2.destroyAllWindows()
            
            messagebox.showinfo("Registro exitoso", "Estudiante registrado correctamente")
            self.nombre_entry.delete(0, END)
            self.carne_entry.delete(0, END)



        else:
            messagebox.showerror("Error de registro", "Todos los campos son obligatorios")

    def regresar(self):
        self.registrar_estudiante.destroy()
        Profesor(self.nodoProfesor)
        
class Ver_Estudiantes:
    def __init__(self, nodoProfesor):
        self.ver_estudiantes = Tk()
        self.ver_estudiantes.title("Lista de Estudiantes")
        self.ver_estudiantes.resizable(0, 0)
        self.ver_estudiantes.geometry("500x350")
        self.nodoProfesor = nodoProfesor
        self.container()

    def container(self):
        self.frame = Frame(height=350, width=500)
        self.frame.pack(padx=25, pady=25)

        # Treeview
        self.tree = ttk.Treeview(self.frame, columns=("Nombre", "Carné"), show='headings')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Carné", text="Carné")
        self.tree.pack(fill=BOTH, expand=True)

        # Botón de regresar
        botonSalir = Button(self.frame, bg="#5ed1fa", font=("Consolas", 12), text="Regresar", command=self.regresar)
        botonSalir.pack(pady=10)

        # Insertar datos en la tabla
        tamanio = self.nodoProfesor.estudiantes.tamanio()
        print(tamanio)

        if tamanio == 0:
            messagebox.showerror("Advertencia", "No hay estudiantes registrados")
        else:
            for i in range(1, tamanio + 1):
                estudiante = self.nodoProfesor.estudiantes.buscar_estudiante(i)
                self.tree.insert("", "end", values=(estudiante.nombre, estudiante.carne))

        # Centrar el contenido de la lista
        self.tree.column("Nombre", anchor=CENTER)
        self.tree.column("Carné", anchor=CENTER)

        self.frame.mainloop()

    def regresar(self):
        self.ver_estudiantes.destroy()
        Profesor(self.nodoProfesor)

# INICIAR EL MAIN DEL PROGRAMA
if __name__ == '__main__':
    main()