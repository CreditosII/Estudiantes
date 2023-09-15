from Modelos.Estudiante import Estudiante
from Repositorios.RepositorioEstudiante import RepositorioEstudiante

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular 
a los modelos, en estos se programarán las tareas básicas tales como crear, listar, 
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorEstudiante():
    """
    constructor que permite llevar a cabo la creacion de instancias del controlador.
    """
    def __init__(self):
        self.repositorioEstudiante = RepositorioEstudiante()
        print("Creando ControladorEstudiante")

    def index(self):
        print("Listar todos los estudiantes")
        return self.repositorioEstudiante.findAll()

    def create(self, elEstudiante):
        print("Crear un estudiante")
        nuevoEstudiante = Estudiante(elEstudiante)
        return self.repositorioEstudiante.save(nuevoEstudiante)

    def show(self, id):
        elEstudiante = Estudiante(self.repositorioEstudiante.findById(id))
        return elEstudiante.__dict__

    def update(self, id, elEstudiante):
        estudianteActual = Estudiante(self.repositorioEstudiante.findById(id))
        estudianteActual.cedula = elEstudiante["cedula"]
        estudianteActual.nombre = elEstudiante["nombre"]
        estudianteActual.apellido = elEstudiante["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)

    def delete(self, id):
        print("Elimiando estudiante con id ", id)
        return self.repositorioEstudiante.delete(id)