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
        print(f'Se ha añadido la asignatura {asignatura.get_nombre()} al profesor')

    def del_asignatura(self, asignatura):
        if asignatura in self.asignaturas:
            self.asignaturas.remove(asignatura)
            print(f'Se ha eliminado la asignatura {asignatura.get_nombre()} del profesor')
        else:
            print(f'La asignatura {asignatura.get_nombre()} no está asignada al profesor')

    def ver_asignaturas(self):
        print(f"Asignaturas del profesor {self.nombre}:")
        for asignatura in self.asignaturas:
            print(f"- {asignatura.get_nombre()} ({asignatura.get_codigo()})")    


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

class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas_matriculadas = []

    def add_asignatura(self, asignatura):
        self.asignaturas_matriculadas.append(asignatura)
        

    def del_asignatura(self, asignatura):
        if asignatura in self.asignaturas_matriculadas:
            self.asignaturas_matriculadas.remove(asignatura)  
        else:
            print(f"La asignatura '{asignatura.get_nombre()}' no está matriculada")

    def asignaturas_matriculado(self):
        print("Asignaturas matriculadas:")
        for asignatura in self.asignaturas_matriculadas:
            print(f"- {asignatura.get_nombre()} ({asignatura.get_codigo()})")

class Universidad:
    def __init__(self):
        self.alumnos = []
        self.profesores = []
        self.asignaturas = []

    def nuevo_alumno(self, nombre, dni, direccion, sexo):
        nuevo_estudiante = Estudiante(nombre, dni, direccion, sexo)
        self.alumnos.append(nuevo_estudiante)
        print(f'Se ha añadido al estudiante {nombre} a la universidad')

    def add_asignatura_alumno(self, dni, asignatura):
        alumno = self.buscar_alumno(dni)
        if alumno:
            alumno.add_asignatura(asignatura)
            print(f'Se ha añadido a {dni} la asignatura {asignatura.get_nombre()}')

    def del_asignatura_alumno(self, dni, asignatura):
        alumno = self.buscar_alumno(dni)
        if alumno:
            alumno.del_asignatura(asignatura)
            print(f'Se ha eliminado al alumno con {dni} la asignatura {asignatura.get_nombre()}')

    def alumno_asignaturas_matriculado(self, dni):
        alumno = self.buscar_alumno(dni)
        if alumno:
            alumno.asignaturas_matriculado()

    def eliminar_alumno(self, dni):
        alumno = self.buscar_alumno(dni)
        if alumno:
            self.alumnos.remove(alumno)
            print(f'Se ha eliminado al estudiante con DNI {dni} de la universidad')
        else:
            print(f'No se encontró ningún estudiante con el DNI {dni}')

    def crear_profesor_titular(self, dni, nombre, direccion, sexo, asignaturas, departamento, area_investigacion):
        nuevo_profesor_titular = Prof_Titular(nombre, dni, direccion, sexo, asignaturas, departamento, area_investigacion)
        self.profesores.append(nuevo_profesor_titular)
        print(f'Se ha creado un nuevo profesor titular con DNI {dni}')

    def crear_profesor_asociado(self, dni, nombre, direccion, sexo, asignaturas, departamento, trabajo_externo):
        nuevo_profesor_asociado = Prof_Asociado(nombre, dni, direccion, sexo, asignaturas, departamento, trabajo_externo)
        self.profesores.append(nuevo_profesor_asociado)
        print(f'Se ha creado un nuevo profesor asociado con DNI {dni}')

    def cambiar_departamento_profesor(self, dni, nuevo_departamento):
        profesor = self.buscar_profesor(dni)
        if profesor:
            profesor.cambio_depart(nuevo_departamento)
            print(f'Se ha cambiado el departamento del profesor con DNI {dni} a {nuevo_departamento}')

    def eliminar_profesor(self, dni):
        profesor = self.buscar_profesor(dni)
        if profesor:
            self.profesores.remove(profesor)
            print(f'Se ha eliminado al profesor con DNI {dni}')
        else:
            print(f'No se encontró ningún profesor con el DNI {dni}')

    def add_asignaturas_profesor(self, dni, asignaturas):
        profesor = self.buscar_profesor(dni)
        if profesor:
            for asignatura in asignaturas:
                profesor.add_asignatura(asignatura)

    def del_asignaturas_profesor(self, dni, asignaturas):
        profesor = self.buscar_profesor(dni)
        if profesor:
            for asignatura in asignaturas:
                profesor.del_asignatura(asignatura)

    def asignaturas_profesor(self, dni):
        profesor = self.buscar_profesor(dni)
        if profesor:
            profesor.ver_asignaturas()

    def buscar_alumno(self, dni):
        for alumno in self.alumnos:
            if alumno.get_dni() == dni:
                return alumno
        print(f'No se encontró ningún alumno con el DNI {dni}')
        return None

    def buscar_profesor(self, dni):
        for profesor in self.profesores:
            if profesor.get_dni() == dni:
                return profesor
        print(f'No se encontró ningún profesor con el DNI {dni}')
        return None

    def nueva_asignatura(self, nombre, codigo):
        nueva_asignatura = Asignatura(nombre, codigo)
        self.asignaturas.append(nueva_asignatura)
        print(f'Se ha creado una nueva asignatura: {nombre}')

    def eliminar_asignatura(self, nombre):
        for asignatura in self.asignaturas:
            if asignatura.get_nombre() == nombre:
                self.asignaturas.remove(asignatura)
                print(f'Se ha eliminado la asignatura: {nombre}')
                return
        print(f'No se encontró ninguna asignatura con el nombre: {nombre}')


if __name__ == "__main__": #Codigo de prueba con casos que deben fallar y los que no.
    # Crear una instancia de Universidad
    universidad = Universidad()

    # Crear algunos alumnos y profesores
    universidad.nuevo_alumno("Juan", "12345678A", "Calle Principal 123", "M")
    universidad.nuevo_alumno("María", "87654321B", "Calle Secundaria 456", "F")
    universidad.crear_profesor_titular("98765432C", "Pedro", "Av. Principal 456", "M", [], Departamento.DIIC, "Como afecta la edad a la memoria")
    universidad.crear_profesor_asociado("23456789D", "Ana", "Av. Secundaria 789", "F", [], Departamento.DITEC, "Empresa X")

    # Agregar asignaturas a los profesores
    universidad.add_asignaturas_profesor("98765432C", [Asignatura("Física", "FIS101"), Asignatura("Optimización", "OPT202")])
    universidad.add_asignaturas_profesor("23456789D", [Asignatura("Programación", "PROG303"), Asignatura("Análisis", "ANA404")])

    # Agregar asignaturas a los alumnos
    universidad.add_asignatura_alumno("12345678A", Asignatura("Biología", "BIO101"))
    universidad.add_asignatura_alumno("12345678A", Asignatura("Historia", "HIS202"))

    # Verificar asignaturas de un alumno
    universidad.alumno_asignaturas_matriculado("12345678A")

    # Verificar asignaturas de un profesor
    universidad.asignaturas_profesor("98765432C")

    # Cambiar departamento de un profesor
    universidad.cambiar_departamento_profesor("23456789D", Departamento.DIS)

    # Eliminar asignatura de un alumno
    universidad.del_asignatura_alumno("12345678A", Asignatura("Biología", "BIO101"))

    # Eliminar asignatura de un profesor
    universidad.del_asignaturas_profesor("98765432C", [Asignatura("Física", "FIS101")])

    # Eliminar alumno y profesor
    universidad.eliminar_alumno("87654321B")
    universidad.eliminar_profesor("98765432C")

    # Eliminar una asignatura
    universidad.eliminar_asignatura("Biología")




#caso de uso con la personita y ovalos 



    #diagrama de uso:  
    # un alumno se matricula meter lista 
    #contratacion del profesor
    #cambio del departamenteo


     


