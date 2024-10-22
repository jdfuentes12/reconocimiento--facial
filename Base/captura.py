import cv2
import os
import imutils
import customtkinter as ctk

class App:
    def __init__(self):
        self.personName = 'Kevin'
        self.dataPath = 'c:/Users/jose2/OneDrive/Documentos/reconocimiento--facial/faces/Rachel'
        self.personPath = os.path.join(self.dataPath, self.personName)

        if not os.path.exists(self.personPath):
            print('Carpeta creada: ', self.personPath)
            os.makedirs(self.personPath)

        self.count = 0
        self.capture_faces()

    def capture_faces(self):
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while self.count < 100:
            ret, frame = cap.read()
            if ret == False:
                break
            
            frame = imutils.resize(frame, width=640)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            auxFrame = frame.copy()

            faces = faceClassif.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                rostro = auxFrame[y:y + h, x:x + w]
                rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(os.path.join(self.personPath, f'rostro_{self.count}.jpg'), rostro)
                self.count += 1

            # Mostrar la captura en la ventana
            cv2.imshow('Captura de Rostros', frame)

            # Salir si se presiona ESC o se han capturado 100 imágenes
            if cv2.waitKey(1) == 27 or self.count >= 100:
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Cambia a "Dark" o "Light" según lo desees
    ctk.set_default_color_theme("blue")  # Cambia el tema a uno que prefieras
    app = App()
