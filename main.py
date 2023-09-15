from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorMateria import ControladorMateria
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorInscripcion import ControladorInscripcion

app = Flask(__name__)
"""
Los cors permiten que se puedan hacer pruebas al 
servidor desde las misma máquina donde está corriendo.
"""
cors = CORS(app)

"""
Implementacion de los controladores
"""

miControladorEstudiante = ControladorEstudiante()
miControladorMateria = ControladorMateria()
miControladorDepartamento = ControladorDepartamento()
miControladorInscripcion = ControladorInscripcion()

"""
Servicios que el servidor ofrecerá; se definen las rutas
y tipos de peticiones a las cuales el servidor responderá CRUD.
"""


#########################Servicios Estudiante###################################
@app.route("/estudiantes", methods=['GET'])
def getEstudiantes():
    json = miControladorEstudiante.index()
    return jsonify(json)


@app.route("/estudiantes", methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json = miControladorEstudiante.create(data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['GET'])
def getEstudiante(id):
    json = miControladorEstudiante.show(id)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json = miControladorEstudiante.update(id, data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
    json = miControladorEstudiante.delete(id)
    return jsonify(json)


##############################################################################

############################Servicios Materia#################################
@app.route("/materias", methods=['GET'])
def getMaterias():
    json = miControladorMateria.index()
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['GET'])
def getMateria(id):
    json = miControladorMateria.show(id)
    return jsonify(json)


@app.route("/materias", methods=['POST'])
def crearMateria():
    data = request.get_json()
    json = miControladorMateria.create(data)
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['PUT'])
def modificarMateria(id):
    data = request.get_json()
    json = miControladorMateria.update(id, data)
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['DELETE'])
def eliminarMateria(id):
    json = miControladorMateria.delete(id)
    return jsonify(json)


@app.route("/materias/<string:id>/departamento/<string:id_departamento>", methods=['PUT'])
def asignarDepartamentoAMateria(id, id_departamento):
    json = miControladorMateria.asignarDepartamento(id, id_departamento)
    return jsonify(json)


##############################################################################


##########################Servicios Departamento##############################

@app.route("/departamentos", methods=['GET'])
def getDepartamentos():
    json = miControladorDepartamento.index()
    return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['GET'])
def getDepartamento(id):
    json = miControladorDepartamento.show(id)
    return jsonify(json)


@app.route("/departamentos/<string:id>/materias", methods=['GET'])
def getMateriasDepartamento(id):
    json = miControladorDepartamento.getMaterias(id)
    return jsonify(json)


@app.route("/departamentos", methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    json = miControladorDepartamento.create(data)
    return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['PUT'])
def modificarDepartamento(id):
    data = request.get_json()
    json = miControladorDepartamento.update(id, data)
    return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['DELETE'])
def eliminarDepartamento(id):
    json = miControladorDepartamento.delete(id)
    return jsonify(json)


##############################################################################

##########################Servicios Inscripcion###############################

@app.route("/inscripciones", methods=['GET'])
def getInscripciones():
    json = miControladorInscripcion.index()
    return jsonify(json)


@app.route("/inscripciones/<string:id>", methods=['GET'])
def getInscripcion(id):
    json = miControladorInscripcion.show(id)
    return jsonify(json)


@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>", methods=['POST'])
def crearInscripcion(id_estudiante, id_materia):
    data = request.get_json()
    json = miControladorInscripcion.create(data, id_estudiante, id_materia)
    return jsonify(json)


@app.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>", methods=['PUT'])
def modificarInscripcion(id_inscripcion, id_estudiante, id_materia):
    data = request.get_json()
    json = miControladorInscripcion.update(id_inscripcion, data, id_estudiante, id_materia)
    return jsonify(json)


@app.route("/inscripciones/<string:id_inscripcion>", methods=['DELETE'])
def eliminarInscripcion(id_inscripcion):
    json = miControladorInscripcion.delete(id_inscripcion)
    return jsonify(json)


##############################################################################

"""
Servicio que el servidor ofrecerá, y este consiste en retornar un JSON el cual
tiene un mensaje que dice que el servidor está corriendo.
"""


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


"""
Método leer el archivo de configuración del proyecto,
retornará un diccionario el cual posee la información dentro del
JSON y se podrá acceder a los atributos necesarios.
"""


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()  # Se asigna lo que retorna el metodo a la variable dataConfig
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    """
    Se crea la instancia del servidor con la url del backend y puerto especificado 
    en el archivo de configuración.
    """
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
