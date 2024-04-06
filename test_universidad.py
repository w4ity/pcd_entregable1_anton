import pytest
from universidad import Universidad, Prof_Titular, Prof_Asociado, Estudiante, Asignatura, Departamento

# Test para verificar la creación de un nuevo alumno
def test_nuevo_alumno():
    universidad = Universidad()
    universidad.nuevo_alumno("Juan", "12345678A", "Calle Principal 123", "M")
    assert len(universidad.alumnos) == 1 #Si se ha creado entonces va a haber un elemeno entonces debe de coincidir con el 1 (razonamiento similar en los proximos tests)

# Test para verificar la creación de un nuevo profesor titular
def test_crear_profesor_titular():
    universidad = Universidad()
    universidad.crear_profesor_titular("98765432C", "Pedro", "Av. Principal 456", "M", [], Departamento.DIIC, "Como afecta la edad a la memoria")
    assert len(universidad.profesores) == 1

# Test para verificar la adición de asignaturas a un profesor
def test_add_asignaturas_profesor():
    universidad = Universidad()
    universidad.crear_profesor_titular("98765432C", "Pedro", "Av. Principal 456", "M", [], Departamento.DIIC, "Como afecta la edad a la memoria")
    universidad.add_asignaturas_profesor("98765432C", [Asignatura("Física", "FIS101"), Asignatura("Optimización", "OPT202")])
    profesor = universidad.buscar_profesor("98765432C")
    assert len(profesor.asignaturas) == 2


# Test para verificar la adición de asignaturas a un alumno
def test_add_asignatura_alumno():
    universidad = Universidad()
    asignatura = Asignatura("Biología", "BIO101")
    universidad.nuevo_alumno("Juan", "12345678A", "Calle Principal 123", "M")
    universidad.add_asignatura_alumno("12345678A", asignatura)
    assert len(universidad.alumnos[0].asignaturas_matriculadas) == 1

# Test para verificar la eliminación de asignaturas de un alumno
def test_del_asignatura_alumno():
    universidad = Universidad()
    asignatura = Asignatura("Biología", "BIO101")
    universidad.nuevo_alumno("Juan", "12345678A", "Calle Principal 123", "M")
    universidad.add_asignatura_alumno("12345678A", asignatura)
    universidad.del_asignatura_alumno("12345678A", asignatura)
    assert len(universidad.alumnos[0].asignaturas_matriculadas) == 0

# Test para verificar la eliminación de asignaturas de un profesor
def test_del_asignaturas_profesor():
    universidad = Universidad()
    asignatura = Asignatura("Física", "FIS101")
    universidad.crear_profesor_titular("98765432C", "Pedro", "Av. Principal 456", "M", [asignatura], Departamento.DIIC, "Como afecta la edad a la memoria")
    universidad.del_asignaturas_profesor("98765432C", [asignatura])
    profesor = universidad.buscar_profesor("98765432C")
    assert len(profesor.asignaturas) == 0

# Test para verificar la eliminación de un alumno
def test_eliminar_alumno():
    universidad = Universidad()
    universidad.nuevo_alumno("Juan", "12345678A", "Calle Principal 123", "M")
    universidad.eliminar_alumno("12345678A")
    assert len(universidad.alumnos) == 0

# Test para verificar la eliminación de un profesor
def test_eliminar_profesor():
    universidad = Universidad()
    universidad.crear_profesor_titular("98765432C", "Pedro", "Av. Principal 456", "M", [], Departamento.DIIC, "Como afecta la edad a la memoria")
    universidad.eliminar_profesor("98765432C")
    assert len(universidad.profesores) == 0

# Test para verificar la eliminación de una asignatura
def test_eliminar_asignatura():
    universidad = Universidad()
    universidad.nueva_asignatura("Biología", "BIO101")
    universidad.eliminar_asignatura("Biología")
    assert len(universidad.asignaturas) == 0

