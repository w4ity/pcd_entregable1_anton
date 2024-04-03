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

class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        super().__init__(nombre, dni, direccion, sexo)
        self.asignaturas_matriculadas = []

    def add_asignatura(self, asignatura):
        self.asignaturas_matriculadas.append(asignatura)
        print(f"La asignatura '{asignatura.get_nombre()}' ha sido añadida")

    def del_asignatura(self, asignatura):
        self.asignaturas_matriculadas.remove(asignatura)
        print(f"La asignatura '{asignatura.get_nombre()}' ha sido eliminada")

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
        for estudiante in self.alumnos:
            if estudiante.get_dni() == dni:
                self.alumnos.add_asigntura(asignatura)
                print(f'Se ha añadido a {dni} la asignatura {asignatura}')


    def del_asignatura_alumno(self, dni, asignatura):
        for estudiante in self.alumnos:
            if estudiante.get_dni() == dni:
                self.alumnos.del_asigntura(asignatura)
                print(f'Se ha añadido a {dni} la asignatura {asignatura}')


    def alumno_asignaturas_matriculado(self, dni):
        for estudiante in self.alumnos:
            if estudiante.get_dni() == dni:
                self.alumnos.asignaturas_matriculado()
                break

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
    
    def crear_profesor_titular(self, dni, nombre, direccion, sexo, asignaturas, departamento, area_investigacion):
        nuevo_profesor_titular = Prof_Titular(nombre, dni, direccion, sexo, asignaturas, departamento, area_investigacion)
        self.profesores.append(nuevo_profesor_titular)
        print(f'Se ha creado un nuevo profesor titular con DNI {dni}')

    def crear_profesor_asociado(self, dni, nombre, direccion, sexo, asignaturas, departamento, trabajo_externo):
        nuevo_profesor_asociado = Prof_Asociado(nombre, dni, direccion, sexo, asignaturas, departamento, trabajo_externo)
        self.profesores.append(nuevo_profesor_asociado)
        print(f'Se ha creado un nuevo profesor asociado con DNI {dni}')

    def eliminar_profesor(self, dni):
        profesor_eliminado = None
        for profesor in self.profesores:
            if profesor.get_dni() == dni:
                profesor_eliminado = profesor
                self.profesores.remove(profesor)
                print(f'Se ha eliminado al profesor con DNI {dni}')
                break
        if profesor_eliminado is None:
            print(f'No se encontró ningún profesor con el DNI {dni}')

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
        asignatura_eliminada = None
        for asignatura in self.asignaturas:
            if asignatura.get_nombre() == nombre:
                asignatura_eliminada = asignatura
                self.asignaturas.remove(asignatura)
                print(f'Se ha eliminado la asignatura: {nombre}')
                break
        if asignatura_eliminada is None:
            print(f'No se encontró ninguna asignatura con el nombre: {nombre}')


if __name__ == "__main__":
    # Crear una instancia de la clase Universidad
    mi_universidad = Universidad()

    # Crear algunos alumnos
    mi_universidad.nuevo_alumno("Juan Perez", "12345678A", "Calle Principal 123", "M")
    mi_universidad.nuevo_alumno("Maria Lopez", "87654321B", "Avenida Secundaria 456", "F")

    # Crear algunos profesores
    mi_universidad.crear_profesor_titular("11111111X", "Pedro Ramirez", "Calle de los Profesores 1", "M", ["Matemáticas"], Departamento.DIIC, "Álgebra")
    mi_universidad.crear_profesor_asociado("22222222Y", "Ana Garcia", "Calle de los Profesores 2", "F", ["Física"], Departamento.DITEC, "Investigación en Física Cuántica")

    # Crear algunas asignaturas
    mi_universidad.nueva_asignatura("Programación Avanzada", "PA101")
    mi_universidad.nueva_asignatura("Diseño de Algoritmos", "DA202")

    # Eliminar un alumno
    mi_universidad.eliminar_alumno("12345678A")

    # Eliminar un profesor
    mi_universidad.eliminar_profesor("11111111X")

    # Buscar un alumno
    alumno_buscado = mi_universidad.buscar_alumno("87654321B")
    if alumno_buscado:
        print(f"Alumno encontrado: {alumno_buscado.get_nombre()}")

    # Buscar un profesor
    profesor_buscado = mi_universidad.buscar_profesor("22222222Y")
    if profesor_buscado:
        print(f"Profesor encontrado: {profesor_buscado.get_nombre()}")

    # Eliminar una asignatura
    mi_universidad.eliminar_asignatura("Programación Avanzada")

#caso de uso con la personita y ovalos 



    #diagrama de uso:  
    # un alumno se matricula meter lista 
    #contratacion del profesor
    #cambio del departamenteo


     


