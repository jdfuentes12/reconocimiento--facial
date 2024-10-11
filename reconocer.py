import cv2
import os

# Ruta a la carpeta donde se almacenan las imágenes de rostros
dataPath = 'faces/jose'  # Cambia a la ruta donde hayas almacenado Data
# colocarles el faces/ y agregarle el nombre de cada uno de los profesores
imagePaths = os.listdir(dataPath)
print('imagePaths=', imagePaths)

# Inicializa el reconocedor de rostros usando LBPH
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# Lee el modelo
face_recognizer.read('modeloLBPHFace.xml')

# Abre la cámara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Cambia a 1 si usas otra cámara

# Carga el clasificador de rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Salir del bucle si no se puede leer el frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    # Detecta los rostros en la imagen
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        rostro = auxFrame[y:y + h, x:x + w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        # Lógica para mostrar el nombre o "Desconocido"
        if result[1] < 70:  # Ajusta el umbral según tus pruebas
            name = imagePaths[result[0]]
            cv2.putText(frame, name, (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            #print(f'Detectado: {name}')  # Imprimir el nombre en la consola
        else:
            cv2.putText(frame, 'Desconocido', (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Muestra el frame procesado
    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(1)
    if k == 27:  # Salir si se presiona la tecla ESC
        break

# Asegúrate de liberar la cámara y destruir las ventanas
cap.release()  # Libera la cámara
cv2.destroyAllWindows()  # Cierra todas las ventanas de OpenCV
