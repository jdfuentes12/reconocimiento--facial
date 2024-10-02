# ------------ ESTRUCTURA PARA LOS PROFESORES ------------

class Profesores():
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
        self.cursos = ListaCuros()
        self.estudiantes = ListaEstudiantes()
        self.next = None


class ListaProfesores():
    def __init__(self):
        self.heard = None
        self.id = 1
        self.size = 0
    
    def agregar_profesor(self, nombre, password):
        nuevo_profesor = Profesores(nombre, password)
        nuevo_profesor.id = self.id
        self.id += 1
        if self.heard is None:
            self.heard = nuevo_profesor
        else:
            current = self.heard
            while current.next is not None:
                current = current.next
            current.next = nuevo_profesor
        self.size += 1

    def mostrar_profesores(self):
        current = self.heard
        while current is not None:
            print(f'ID: {current.id}, Nombre: {current.nombre}')
            current = current.next

# ------------ ESTRUCTURA PARA LOS CURSOS ------------

class Cursos:
    def __init__(self, nombre="Curso Genérico", estado="Activo", seccion="A"):
        self.nombre = nombre
        self.estado = estado
        self.seccion = seccion
        self.next = None

class ListaCuros:
    def __init__(self):
        self.heard = None
        self.id = 1
        self.size = 0

    def insertar_curso(self, nombre, estado, seccion):
        nuevo_curso = Cursos(nombre, estado, seccion)
        if not self.heard:
            self.heard = nuevo_curso
        else:
            actual = self.heard
            while actual.next:
                actual = actual.next
            actual.next = nuevo_curso
        self.size += 1

    def mostrar_cursos(self):
        actual = self.heard
        while actual:
            print(f"Nombre: {actual.nombre}, Estado: {actual.estado}, Sección: {actual.seccion}")
            actual = actual.next



# ------------ ESTRUCTURA PARA LOS ESTUDIANTES ------------


class Estudiantes:
    def __init__(self, nombre, carne):
        self.nombre = nombre
        self.carne = carne
        self.next = None

class ListaEstudiantes:
    def __init__(self):
        self.heard = None
        self.id = 1
        self.size = 0

    def insertar_estudiante(self, nombre, carne):
        nuevo_estudiante = Estudiantes(nombre, carne)
        if not self.heard:
            self.heard = nuevo_estudiante
        else:
            actual = self.heard
            while actual.next:
                actual = actual.next
            actual.next = nuevo_estudiante
        self.size += 1
    
    def mostrar_estudiantes(self):
        actual = self.heard
        while actual:
            print(f"Nombre: {actual.nombre}, Carné: {actual.carne}")
            actual = actual.next

