from enum import Enum

class Persona:
    def __init__(self,nombre, dni, direccion, sexo):
        self.nombre = nombre
        self._dni = dni
        self._direccion = direccion
        self.sexo = sexo

    def get_nombre():

    
    def get_dni():

    
    def get_direccion():
    
    def get_sexo():


class Profesor(Persona):
    def __init__(self, nombre,dni, direccion, sexo, asignaturas):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas = asignaturas


    def add_miembro():

    def del_miembro():

    def cambio_depart():

    def add_asignatura():

    def del_asignatura():


class Departamento(Enum):
     


