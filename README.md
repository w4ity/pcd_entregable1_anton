Ejercicio: 

Se pretende desarrollar un sistema de gestión de usuarios de universidad que permita
gestionar investigadores, profesores asociados, profesores titulares y estudiantes. Los
profesores asociados imparten asignaturas y los profesores Titulares, además de
impartir asignaturas (como los profesores asociados), tienen el rol de Investigador. Un
asociado no puede ser Investigador.
Los investigadores tienen un área de investigación asociada. Y los profesores (tanto
asociados como Titulares), tienen un listado de asignaturas que imparten. Asimismo,
los estudiantes tienen una serie de asignaturas en las que están matriculados.
Todos son personas por lo que se debe considerar la creación de la entidad Persona,
con atributos comunes a todos como Nombre, DNI, dirección o sexo (V,M).
Se debe proporcionar los métodos para añadir y eliminar tanto miembros de
departamento como estudiantes. Además, se debe de proporcionar la funcionalidad
para que un miembro de un departamento (ya sea Investigador, Profesor Asociado o
Profesor Titular) cambie de Departamento. Se debe modelar la clase miembro de
departamento para garantizar extensibilidad. Los departamentos existentes a los que
puede estar asociados los miembros de departamento son tres, DIIC, DITEC, DIS. Un
miembro de departamento solo puede estar asociado a un departamento.
