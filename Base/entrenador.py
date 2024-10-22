import cv2
import os
import numpy as np

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