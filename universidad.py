from enum import Enum

class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self._dni = dni
        self._direccion = direccion
        self.sexo = sexo

    def get_nombre(self):
        return self.nombre

    
    def get_dni(self):
        return self._dni

    
    def get_direccion(self):
        return self._direccion
    
    def get_sexo(self):
        return self.sexo


class Profesor(Persona):
    def __init__(self, nombre,dni, direccion, sexo, asignaturas, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas = asignaturas
        self.departamento = departamento

    def add_miembro(self, ):
        return 

    def del_miembro(self):
        return
    
    def cambio_depart(self, departamento):
        self.departamento = departamento
        print(f'El departamento se ha cambiado a {departamento}')

    def add_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
        print(f'Se ha eliminado la asignatura {asignatura}')

    def del_asignatura(self, asignatura):
        assert asignatura in self.asignaturas, f"La asignatura '{asignatura}' no está en la lista de asignaturas"
        self.asignaturas.remove(asignatura)


class Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3


class Prof_Asociado(Profesor):
    def __init__(self, nombre,dni, direccion, sexo, asignaturas, departamento, trabajo_externo):
        super().__init__(nombre,dni, direccion, sexo, asignaturas, departamento)
        self.trabajo_externo = trabajo_externo

    def get_trabajo_externo(self):
        return self.trabajo_externo
    

class Prof_Titular(Profesor):
    def __init__(self, nombre,dni, direccion, sexo, asignaturas, departamento, area_investigacion):
        super().__init__(nombre,dni, direccion, sexo, asignaturas, departamento)
        self.area_investigacion = area_investigacion


class Asignatura:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def get_nombre(self):
        return self.nombre
    

    def get_codigo(self):
        return self.codigo


    def modif_nombre(self, nombre):
        self.nombre = nombre
        print('Su nombre se ha cambiado')

    def modif_codigoe(self, codigo):
        self.codigo = codigo
        print('El codigo se ha cambiado')


class Estudiante:
    def __init__(self, nombre):
        self.asignaturas = []
        self.nombre = nombre
    
    def add_estud(nombre):
        return

    def del_estud(nombre):
        return

    def add_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
        print('Su asignatura ha sido añadida')


    def del_asignatura(self, asignatura):
        self.asignaturas.remove(asignatura)
        print('Su asignatura ha sido aliminada')



    #diagrama de uso:  
    # un alumno se matricula meter lista 
    #contratacion del profesor
    #cambio del departamenteo


     


