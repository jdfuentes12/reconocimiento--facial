import cv2
import os
import numpy as np
import tkinter as tk
import imutils
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

class FaceRecognitionGUI:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.geometry("400x200")

        # Cargar el modelo de detección de rostros
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        if self.face_cascade.empty():
            messagebox.showerror("Error", "No se pudo cargar el modelo de detección de rostros.")
        
        # Botón para registrar el rostro
        self.register_button = tk.Button(window, text="Registrar Rostro", width=20, command=self.start_registration)
        self.register_button.pack(pady=10)

        # Botón para verificar el rostro
        self.verify_button = tk.Button(window, text="Verificar Rostro", width=20, command=self.show_verify_window)
        self.verify_button.pack(pady=10)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_registration(self):
        self.name = simpledialog.askstring("Registro", "Ingrese el nombre de la persona:")
        if self.name:
            self.show_camera_window()    

    def show_camera_window(self):
        self.camera_window = tk.Toplevel(self.window)
        self.camera_window.title("Registro de Rostro")
        self.camera_window.geometry("600x400")

        self.camera_label = tk.Label(self.camera_window)
        self.camera_label.pack()

        self.capture_button = tk.Button(self.camera_window, text="Capturar Rostro", command=self.capture_face)
        self.capture_button.pack(pady=10)


    def capture_face(self):
        # Captura y guarda la imagen del rostro
        print(self.name)
        personName = self.name
        dataPath = 'C:/Users/jose2/OneDrive/Documentos/reconocimiento--facial/faces' #Cambia a la ruta donde hayas almacenado Data
        personPath = dataPath + '/' + personName

        if not os.path.exists(personPath):
            print('Carpeta creada: ',personPath)
            os.path.exists(personPath)

        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        #cap = cv2.VideoCapture('Video.mp4')

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
                cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
                count = count + 1
            cv2.imshow('frame',frame)

            k =  cv2.waitKey(1)
            if k == 27 or count >= 300:
                break
            cap.release()
            cv2.destroyAllWindows()

    def show_verify_window(self):
        self.verify_window = tk.Toplevel(self.window)
        self.verify_window.title("Verificación de Rostro")
        self.verify_window.geometry("600x400")

        self.verify_camera_label = tk.Label(self.verify_window)
        self.verify_camera_label.pack()

   

    def on_closing(self):
        self.window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionGUI(root, "Sistema de Reconocimiento Facial")
    root.mainloop()
