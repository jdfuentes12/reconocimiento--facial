from customtkinter import *
from CTkMessagebox import CTkMessagebox  # Importar CTkMessagebox
from estructuras import profesores
import numpy as np
import cv2
import os
import imutils

ListaProfesores = profesores.ListaProfesores()
ListaProfesores.agregar_profesor("Carlos","123","carlos")

class main():
    def __init__(self):
        self.root = CTk()
        self.root.geometry("400x300")
        self.root.title("Login")

        # Obtener el tamaño de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        position_x = (screen_width // 2) - (400 // 2)
        position_y = (screen_height // 2) - (300 // 2)

        # Establecer la geometría de la ventana con la posición calculada
        self.root.geometry(f"400x300+{position_x}+{position_y}")

        self.username_label = CTkLabel(self.root, text="Username:", font=("Helvetica", 16, "bold"))
        self.username_label.pack(pady=10)

        self.username_entry = CTkEntry(self.root)
        self.username_entry.pack(pady=10)

        self.password_label = CTkLabel(self.root, text="Password:", font=("Helvetica", 16, "bold"))
        self.password_label.pack(pady=10)
        self.password_entry = CTkEntry(self.root, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = CTkButton(self.root, text="Login", command=self.login)
        self.login_button.pack(pady=20)

        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        loginProfesor = ListaProfesores.buscar_nombre_password(username, password)
        
        if username == "":
            CTkMessagebox(title="Error al iniciar sesión", message="Usuario o contraseña incorreta", icon="cancel")  # Mostrar error
        elif password == "":
            CTkMessagebox(title="Error al iniciar sesión", message="Usuario o contraseña incorreta", icon="cancel")
        elif username == "" and password == "":
            CTkMessagebox(title="Error al iniciar sesión", message="Usuario o contraseña")
        elif username  == "admin" and password == "admin":
            self.root.destroy()
            Admin()
        elif loginProfesor != None:
            self.root.destroy()
            Profesor(loginProfesor)

class Admin():
    def __init__(self):
        self.root = CTk()
        self.root.geometry("400x300")
        self.root.title("Menu Administrador")

        # Obtener el tamaño de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        position_x = (screen_width // 2) - (400 // 2)
        position_y = (screen_height // 2) - (300 // 2)

        # Establecer la geometría de la ventana con la posición calculada
        self.root.geometry(f"400x300+{position_x}+{position_y}")

        self.bienvenida = CTkLabel(self.root, text="Bienvenido al modo administrador", font=("Helvetica", 18, "bold"))
        self.bienvenida.pack(pady=15)

        self.register_button = CTkButton(self.root, text="Registrar Profesores", command=self.register_profesor, font=("Helvetica", 13))
        self.register_button.pack(pady=15)

        self.view_button = CTkButton(self.root, text="Ver Profesores", command=self.view_profesores, font=("Helvetica", 13))
        self.view_button.pack(pady=15)

        self.back_button = CTkButton(self.root, text="Regresar", command=self.back, font=("Helvetica", 13))
        self.back_button.pack(pady=15)

        self.root.mainloop()

    def register_profesor(self):
        # Lógica para registrar profesores
        self.register_window = CTkToplevel(self.root)
        self.register_window.geometry("400x400")
        self.register_window.title("Registrar Profesor")

        self.name_label = CTkLabel(self.register_window, text="Nombre Completo:", font=("Helvetica", 18, "bold"))
        self.name_label.pack(pady=10)
        self.name_entry = CTkEntry(self.register_window)
        self.name_entry.pack(pady=10)

        self.username_label = CTkLabel(self.register_window, text="Usuario:", font=("Helvetica", 18, "bold"))
        self.username_label.pack(pady=10)
        self.username_entry = CTkEntry(self.register_window)
        self.username_entry.pack(pady=10)

        self.password_label = CTkLabel(self.register_window, text="Contraseña:", font=("Helvetica", 18, "bold"))
        self.password_label.pack(pady=10)
        self.password_entry = CTkEntry(self.register_window, show="*")
        self.password_entry.pack(pady=10)

        self.save_button = CTkButton(self.register_window, text="Guardar", command=self.save_profesor)
        self.save_button.pack(pady=20)

    def save_profesor(self):
        nombre_completo = self.name_entry.get()
        usuario = self.username_entry.get()
        contraseña = self.password_entry.get()

        if nombre_completo and usuario and contraseña:
            ListaProfesores.agregar_profesor(nombre_completo, usuario, contraseña)
            CTkMessagebox(title="Registro Exitoso", message="Profesor registrado correctamente", icon="info")
            self.register_window.destroy()
        else:
            CTkMessagebox(title="Error", message="Todos los campos son obligatorios", icon="cancel")

    def view_profesores(self):
        # Lógica para ver la lista de profesores
        
        self.view_window = CTkToplevel(self.root)
        self.view_window.geometry("450x500")
        self.view_window.title("Lista de Profesores")

        self.table_frame = CTkFrame(self.view_window)
        self.table_frame.pack(fill="both", expand=True, padx=15, pady=15)

        self.table = CTkFrame(self.table_frame)
        self.table.pack(fill="both", expand=True)

        self.headers = ["Nombre", "Usuario", "Contraseña"]
        for i, header in enumerate(self.headers):
            label = CTkLabel(self.table, text=header, font=("Helvetica", 14, "bold"))
            label.grid(row=0, column=i, padx=30, pady=15)
        
        tamanio = ListaProfesores.tamanio()

        if tamanio == 0:
            CTkMessagebox(title="Advertencia", message="No hay profesores registrados", icon="warning")
        else:
            for i in range(1, tamanio + 1):
                profesor = ListaProfesores.buscar_profesor(i)
                CTkLabel(self.table, text=profesor.nombre).grid(row=i, column=0, padx=10, pady=5)
                CTkLabel(self.table, text=profesor.usuario).grid(row=i, column=1, padx=10, pady=5)
                CTkLabel(self.table, text=profesor.password).grid(row=i, column=2, padx=10, pady=5)
        

    def back(self):
        self.root.destroy()
        main()

class Profesor():
    def __init__(self,nodoProfesor):
        self.nodoProfesor = nodoProfesor

        self.root = CTk()
        self.root.geometry("400x300")
        self.root.title("Menu Profesor")

        # Obtener el tamaño de la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        position_x = (screen_width // 2) - (400 // 2)
        position_y = (screen_height // 2) - (300 // 2)

        # Establecer la geometría de la ventana con la posición calculada
        self.root.geometry(f"400x300+{position_x}+{position_y}")
        
        
        self.bienvenida = CTkLabel(self.root, text = f"Bienvenido: {nodoProfesor.nombre}", font=("Helvetica", 18, "bold"))
        self.bienvenida.pack(pady=15)

        self.add_student_button = CTkButton(self.root, text="Agregar Estudiante", command=self.add_student, font=("Helvetica", 13))
        self.add_student_button.pack(pady=15)

        self.view_students_button = CTkButton(self.root, text="Ver Estudiantes", command=self.view_students, font=("Helvetica", 13))
        self.view_students_button.pack(pady=15)

        self.attendance_button = CTkButton(self.root, text="Tomar Asistencia",command=self.attendance, font=("Helvetica",13))
        self.attendance_button.pack(pady=15)

        self.back_button = CTkButton(self.root, text="Regresar", command=self.back, font=("Helvetica", 13))
        self.back_button.pack(pady=15)

        self.root.mainloop()

    def add_student(self):
        # Lógica para agregar estudiante

        self.add_student_window = CTkToplevel(self.root)
        self.add_student_window.geometry("400x300")
        self.add_student_window.title("Agregar Estudiante")

        self.student_name_label = CTkLabel(self.add_student_window, text="Nombre Completo:", font=("Helvetica", 18, "bold"))
        self.student_name_label.pack(pady=10)
        self.student_name_entry = CTkEntry(self.add_student_window)
        self.student_name_entry.pack(pady=10)

        self.student_id_label = CTkLabel(self.add_student_window, text="Número de Carné:", font=("Helvetica", 18, "bold"))
        self.student_id_label.pack(pady=10)
        self.student_id_entry = CTkEntry(self.add_student_window)
        self.student_id_entry.pack(pady=10)

        self.save_student_button = CTkButton(self.add_student_window, text="Registrar", command=self.save_student)
        self.save_student_button.pack(pady=20)

    def save_student(self):
        nombre_completo = self.student_name_entry.get()
        numero_carne = self.student_id_entry.get()
        
        if nombre_completo and numero_carne:
            # Aquí puedes agregar la lógica para guardar el estudiante
            self.nodoProfesor.estudiantes.insertar_estudiante(nombre_completo,numero_carne)
            self.nodoProfesor.estudiantes.mostrar_estudiantes()
            nombreProfesor = self.nodoProfesor.nombre

            dataPath = 'c:/Users/jose2/OneDrive/Documentos/reconocimiento--facial/faces' #Cambia a la ruta donde hayas almacenado Data
            datapath1 = dataPath + '/' + nombreProfesor
            datapath2 = datapath1 + '/' + nombre_completo

            if not os.path.exists(datapath2):
                print('Carpeta creada', datapath2)
                os.makedirs(datapath2)


            cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
            faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            count = 0

            while count < 100:
                ret, frame = cap.read()
                if ret == False:
                    break

                frame = imutils.resize(frame,width=640)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                auxFrame = frame.copy()

                faces = faceClassif.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    rostro = auxFrame[y:y + h, x:x + w]
                    rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                    cv2.imwrite(os.path.join(datapath2, f'rostro_{count}.jpg'), rostro)
                    count += 1
                
                cv2.imshow('Captura de Rostros', frame)
                
                if cv2.waitKey(1) == 27 or count >= 100:
                    break
            
            cap.release()
            cv2.destroyAllWindows()
            entrenar()
            CTkMessagebox(title="Registro Exitoso", message="Estudiante registrado correctamente", icon="info")
            self.add_student_window.destroy()
        else:
            CTkMessagebox(title="Error", message="Todos los campos son obligatorios", icon="cancel")
    
    def view_students(self):
        # Lógica para ver estudiantes
        self.view_students_window = CTkToplevel(self.root)
        self.view_students_window.geometry("450x500")
        self.view_students_window.title("Lista de Estudiantes")

        self.table_frame = CTkFrame(self.view_students_window)
        self.table_frame.pack(fill="both", expand=True, padx=15, pady=15)

        self.table = CTkFrame(self.table_frame)
        self.table.pack(fill="both", expand=True)

        self.headers = ["Nombre", "Número de Carné"]
        for i, header in enumerate(self.headers):
            label = CTkLabel(self.table, text=header, font=("Helvetica", 14, "bold"))
            label.grid(row=0, column=i, padx=30, pady=15)

        tamanio = self.nodoProfesor.estudiantes.tamanio()
        if tamanio == 0:
            CTkMessagebox(title="Advertencia", message="No hay estudiantes registrados", icon="warning")
        else:
            for i in range(1, tamanio +1):
                estudiante = self.nodoProfesor.estudiantes.buscar_estudiante(i)
                CTkLabel(self.table, text=estudiante.nombre).grid(row=i, column=0, padx=10, pady=5)
                CTkLabel(self.table, text=estudiante.carne).grid(row=i, column=1, padx=10, pady=5)

    def attendance(self):
        nodo_profesor = self.nodoProfesor
        dataPath = 'faces' + '/' + nodo_profesor.nombre
        imagePaths = os.listdir(dataPath)
        print('imagePaths=', imagePaths)

        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        face_recognizer.read('modeloLBPHFace.xml')

        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while True:
            ret, frame =cap.read()
            if not ret:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = gray.copy()
            faces = faceClassif.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:
                rostro = auxFrame[y:y+h,x:x+w]
                rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
                result = face_recognizer.predict(rostro)

                if result[1] < 70:
                    name = imagePaths[result[0]]
                    cv2.putText(frame,name,(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                else:
                    cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.imshow('frame',frame)

            k = cv2.waitKey(1)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

    def back(self):
        self.root.destroy()
        main()

class entrenar():
    def __init__(self):
        dataPath = 'faces'  # Cambia a la ruta donde hayas almacenado Data
        teacherList = os.listdir(dataPath)
        print('Lista de profesores: ', teacherList)

        labels = []
        facesData = []
        label = 0

        for nameDir in teacherList:
            personPath = os.path.join(dataPath, nameDir)
            print(personPath)
            studentList = os.listdir(personPath)
            print('Lista de estudiantes: ', studentList)

            for nameDir2 in studentList:
                personPath2 = os.path.join(personPath, nameDir2)

                # Aquí está el bloque con la indentación corregida
                for fileName in os.listdir(personPath2):
                    print('Rostros: ', nameDir2 + '/' + fileName)
                    labels.append(label)
                    facesData.append(cv2.imread(os.path.join(personPath2, fileName), 0))

                label += 1  # Actualizar el label después de procesar los archivos
        # Métodos para entrenar el reconocedor
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()

        # Entrenando el reconocedor de rostros
        print("Entrenando...")
        face_recognizer.train(facesData, np.array(labels))

        # Almacenando el modelo obtenido
        face_recognizer.write('modeloLBPHFace.xml')
        print("Modelo almacenado...")


# INICIAR EL MAIN DEL PROGRAMA
if __name__ == '__main__':
    main()