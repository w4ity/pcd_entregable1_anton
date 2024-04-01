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


class Departamento(Enum):
    DIIC = 1
    DITEC = 2
    DIS = 3

class Profesor(Persona):
    def __init__(self, nombre, dni, direccion, sexo, asignaturas, departamento):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas = asignaturas
        if isinstance(departamento, Departamento):
            self.departamento = departamento
        else:
            raise ValueError("El departamento debe ser uno de: DIIC, DITEC, DIS")

    def add_miembro(self, nuevo_miembro):
        if nuevo_miembro not in self.departamento:
            self.departamento.append(nuevo_miembro)
            print(f'Se ha añadido {nuevo_miembro} al departamento {self.departamento}')
        else:
            print(f'{nuevo_miembro} ya es miembro del departamento {self.departamento}')

    def del_miembro(self, miembro):
        if miembro in self.departamento:
            self.departamento.remove(miembro)
            print(f'Se ha eliminado {miembro} del departamento {self.departamento}')
        else:
            print(f'{miembro} no es miembro del departamento {self.departamento}')

    def cambio_depart(self, nuevo_departamento):
        self.departamento = nuevo_departamento
        print(f'El departamento se ha cambiado a {nuevo_departamento}')

    def add_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)
        print(f'Se ha añadido la asignatura {asignatura}')

    def del_asignatura(self, asignatura):
        assert asignatura in self.asignaturas, f"La asignatura '{asignatura}' no está en la lista de asignaturas"
        self.asignaturas.remove(asignatura)
        print(f'Se ha eliminado la asignatura {asignatura}')


class Prof_Asociado(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, asignaturas, departamento, trabajo_externo):
        super().__init__(nombre, dni, direccion, sexo, asignaturas, departamento)
        self.trabajo_externo = trabajo_externo

    def get_trabajo_externo(self):
        return self.trabajo_externo
    

class Prof_Titular(Profesor):
    def __init__(self, nombre, dni, direccion, sexo, asignaturas, departamento, area_investigacion):
        super().__init__(nombre, dni, direccion, sexo, asignaturas, departamento)
        self.area_investigacion = area_investigacion

    def get_area_inv(self):
        return self.area_investigacion

    def modificar_area_inv(self, nueva_area):
        self.area_investigacion = nueva_area

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

    def modif_codigo(self, codigo):
        self.codigo = codigo

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.asignaturas_matriculadas = []

    def add_estud(self, nombre):
        print(f"Se ha añadido al estudiante {nombre}")

    def del_estud(self, nombre):
        print(f"Se ha eliminado al estudiante {nombre}")

    def add_asignatura(self, asignatura):
        self.asignaturas_matriculadas.append(asignatura)
        print(f"La asignatura '{asignatura.get_nombre()}' ha sido añadida")

    def del_asignatura(self, asignatura):
        self.asignaturas_matriculadas.remove(asignatura)
        print(f"La asignatura '{asignatura.get_nombre()}' ha sido eliminada")

    def asignaturas(self):
        print("Asignaturas matriculadas:")
        for asignatura in self.asignaturas_matriculadas:
            print(f"- {asignatura.get_nombre()} ({asignatura.get_codigo()})")


class Universidad:
    def __init__(self):
        self.alumnos = []
        self.profesores = []
        self.asignaturas = []

    def nuevo_alumno(self, nombre, dni, direccion, sexo):
        nuevo_estudiante = Estudiante(nombre)
        nuevo_estudiante_persona = Persona(nombre, dni, direccion, sexo)
        self.estudiantes.append(nuevo_estudiante)
        print(f'Se ha añadido al estudiante {nombre} a la universidad')


    def eliminar_alumno(self, dni):
        estudiante_eliminado = None
        for estudiante in self.alumnos:
            if estudiante.get_dni() == dni:
                estudiante_eliminado = estudiante
                self.alumnos.remove(estudiante)
                print(f'Se ha eliminado al estudiante con DNI {dni} de la universidad')
                break
        if estudiante_eliminado is None:
            print(f'No se encontró ningún estudiante con el DNI {dni}')





    #diagrama de uso:  
    # un alumno se matricula meter lista 
    #contratacion del profesor
    #cambio del departamenteo


     


