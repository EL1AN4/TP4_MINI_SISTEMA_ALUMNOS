
"""
Módulo de gestión de alumnos.

Contiene las funciones CRUD y las operaciones estadísticas del sistema.
Los datos se administran mediante una lista de diccionarios en memoria,
sin utilizar bases de datos ni mecanismos de persistencia.
"""


# --- OPERACIONES CRUD ---

def agregar_alumno(
    alumnos: list[dict],
    dni: str,
    nombre: str,
    apellido: str,
    curso: str,
    nota: float
) -> bool:
    """Registra un alumno si su DNI no se encuentra repetido.

    Args:
        alumnos: Lista donde se almacenarán los estudiantes.
        dni: Número de documento del alumno.
        nombre: Nombre del estudiante.
        apellido: Apellido del estudiante.
        curso: Curso al que pertenece.
        nota: Calificación del estudiante.

    Returns:
        bool: True si el alumno fue agregado, False si el DNI existe.
    """
    # El DNI funciona como identificador único de cada alumno.
    if buscar_alumno(alumnos, dni) is not None:
        return False

    alumno = {
        "dni": dni,
        "nombre": nombre,
        "apellido": apellido,
        "curso": curso,
        "nota": nota
    }

    alumnos.append(alumno)
    return True


def listar_alumnos(alumnos: list[dict]) -> list[dict]:
    """Retorna la lista completa de alumnos registrados.

    Args:
        alumnos: Lista de estudiantes registrados.

    Returns:
        list[dict]: Lista con los datos de todos los alumnos.
    """
    return alumnos


def buscar_alumno(alumnos: list[dict], dni: str) -> dict | None:
    """Busca un alumno mediante su número de DNI.

    Args:
        alumnos: Lista donde se realizará la búsqueda.
        dni: Número de documento que se desea localizar.

    Returns:
        dict | None: Diccionario del alumno encontrado o None.
    """
    for alumno in alumnos:
        if alumno["dni"] == dni:
            return alumno

    return None


def modificar_nota(
    alumnos: list[dict],
    dni: str,
    nueva_nota: float
) -> bool:
    """Actualiza la nota de un alumno identificado por su DNI.

    Args:
        alumnos: Lista donde se encuentra el estudiante.
        dni: Número de documento del alumno.
        nueva_nota: Nueva calificación que se desea registrar.

    Returns:
        bool: True si se modificó la nota, False si no existe el alumno.
    """
    alumno = buscar_alumno(alumnos, dni)

    if alumno is None:
        return False

    alumno["nota"] = nueva_nota
    return True


def eliminar_alumno(alumnos: list[dict], dni: str) -> bool:
    """Elimina de la lista al alumno identificado por su DNI.

    Args:
        alumnos: Lista donde se encuentra el estudiante.
        dni: Número de documento del alumno que se desea eliminar.

    Returns:
        bool: True si se eliminó el alumno, False si no fue encontrado.
    """
    alumno = buscar_alumno(alumnos, dni)

    if alumno is None:
        return False

    # Se elimina el diccionario encontrado para evitar alterar el recorrido.
    alumnos.remove(alumno)
    return True


# --- ESTADÍSTICAS Y CLASIFICACIÓN ---

def calcular_promedio(alumnos: list[dict]) -> float | None:
    """Calcula el promedio general de las notas registradas.

    Args:
        alumnos: Lista de alumnos que se utilizará para el cálculo.

    Returns:
        float | None: Promedio de las notas o None si no hay alumnos.
    """
    # Se controla la lista vacía para evitar una división por cero.
    if not alumnos:
        return None

    suma_notas = sum(alumno["nota"] for alumno in alumnos)

    return suma_notas / len(alumnos)


def mejor_nota(alumnos: list[dict]) -> tuple[float, list[dict]] | None:
    """Obtiene la nota máxima y todos los alumnos que la consiguieron.

    Args:
        alumnos: Lista de alumnos que se utilizará para la consulta.

    Returns:
        tuple[float, list[dict]] | None: Nota máxima y lista de alumnos
            que la obtuvieron, o None si no existen registros.
    """
    if not alumnos:
        return None

    nota_maxima = max(alumno["nota"] for alumno in alumnos)

    mejores_alumnos = [
        alumno for alumno in alumnos
        if alumno["nota"] == nota_maxima
    ]

    return nota_maxima, mejores_alumnos


def aprobados_desaprobados(
    alumnos: list[dict]
) -> tuple[list[dict], list[dict]]:
    """Clasifica a los estudiantes según sus calificaciones.

    Args:
        alumnos: Lista de alumnos que se desea clasificar.

    Returns:
        tuple[list[dict], list[dict]]: Dos listas, primero los aprobados
            y luego los desaprobados.
    """
    aprobados = []
    desaprobados = []

    # La nota mínima de aprobación establecida para el sistema es 6.
    for alumno in alumnos:
        if alumno["nota"] >= 6:
            aprobados.append(alumno)
        else:
            desaprobados.append(alumno)

    return aprobados, desaprobados
