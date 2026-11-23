
"""
Módulo principal del Mini Sistema de Alumnos en Memoria.

Contiene el menú interactivo, coordina las operaciones del sistema
y presenta los resultados de las consultas al usuario.
"""

# --- IMPORTACIONES ---

from alumnos import (
    agregar_alumno,
    aprobados_desaprobados,
    buscar_alumno,
    calcular_promedio,
    eliminar_alumno,
    listar_alumnos,
    mejor_nota,
    modificar_nota,
)
from utilidades import (
    solicitar_dni,
    solicitar_nota,
    solicitar_opcion,
    solicitar_texto,
)

# --- PRESENTACIÓN DEL MENÚ ---

def mostrar_menu() -> None:
    """Muestra las opciones disponibles del sistema.

    Returns:
        None: No retorna ningún valor.
    """
    print("\n")
    print("=" * 48)
    print("          MINI SISTEMA DE ALUMNOS")
    print("=" * 48)
    print("  1. Cargar alumno")
    print("  2. Listar alumnos")
    print("  3. Buscar alumno por DNI")
    print("  4. Modificar nota")
    print("  5. Eliminar alumno por DNI")
    print("-" * 48)
    print("  6. Calcular promedio general")
    print("  7. Mostrar mejor nota")
    print("  8. Mostrar aprobados y desaprobados")
    print("-" * 48)
    print("  9. Salir")
    print("=" * 48)


# --- PRESENTACIÓN DE ALUMNOS ---

def mostrar_lista_alumnos(titulo: str, alumnos: list[dict]) -> None:
    """Muestra los datos de una lista de alumnos.

    Args:
        titulo: Nombre de la sección que se desea mostrar.
        alumnos: Lista de diccionarios con los datos de los alumnos.

    Returns:
        None: No retorna ningún valor.
    """
    print(f"\n{'-' * 65}")
    print(f"{titulo:^65}")
    print("-" * 65)

    if not alumnos:
        print("\n  No hay alumnos para mostrar.")
        print("-" * 65)
        return

    for indice, alumno in enumerate(alumnos, start=1):
        print(f"\n  ALUMNO N.º {indice}")
        print(f"  DNI:       {alumno['dni']}")
        print(f"  Nombre:    {alumno['nombre']} {alumno['apellido']}")
        print(f"  Curso:     {alumno['curso']}")
        print(f"  Nota:      {alumno['nota']:g}")
        print("  " + "-" * 35)

    print(f"\n  Total de alumnos: {len(alumnos)}")
    print("-" * 65)


def mostrar_datos_alumno(alumno: dict) -> None:
    """Muestra los datos completos de un alumno.

    Args:
        alumno: Diccionario que contiene los datos del estudiante.

    Returns:
        None: No retorna ningún valor.
    """
    print("\n" + "-" * 45)
    print("              DATOS DEL ALUMNO")
    print("-" * 45)
    print(f"  DNI:       {alumno['dni']}")
    print(f"  Nombre:    {alumno['nombre']}")
    print(f"  Apellido:  {alumno['apellido']}")
    print(f"  Curso:     {alumno['curso']}")
    print(f"  Nota:      {alumno['nota']:g}")
    print("-" * 45)


# --- FUNCIONES DE GESTIÓN ---

def cargar_alumno(alumnos: list[dict]) -> None:
    """Solicita los datos y registra un nuevo alumno.

    Args:
        alumnos: Lista donde se almacenará el nuevo estudiante.

    Returns:
        None: No retorna ningún valor.
    """
    print("\n" + "=" * 48)
    print("                CARGAR ALUMNO")
    print("=" * 48)

    dni = solicitar_dni()

    if buscar_alumno(alumnos, dni) is not None:
        print("\n  [ERROR] Ya existe un alumno con ese DNI.")
        print("  No se realizó ningún registro.")
        print("-" * 48)
        return

    print("\n  Complete los datos del nuevo alumno:")
    print("  " + "-" * 35)

    nombre = solicitar_texto("  Nombre: ")
    apellido = solicitar_texto("  Apellido: ")
    curso = solicitar_texto("  Curso: ")
    nota = solicitar_nota()

    if agregar_alumno(alumnos, dni, nombre, apellido, curso, nota):
        print("\n" + "-" * 48)
        print("  [OK] Alumno agregado correctamente.")
        print("-" * 48)


def consultar_alumno(alumnos: list[dict]) -> None:
    """Busca un alumno por DNI y muestra sus datos.

    Args:
        alumnos: Lista de alumnos donde se realizará la búsqueda.

    Returns:
        None: No retorna ningún valor.
    """
    print("\n" + "=" * 48)
    print("              BUSCAR ALUMNO")
    print("=" * 48)

    dni = solicitar_dni()
    alumno = buscar_alumno(alumnos, dni)

    if alumno is None:
        print("\n  [AVISO] No se encontró un alumno con ese DNI.")
        print("-" * 48)
    else:
        print("\n  [OK] Alumno encontrado.")
        mostrar_datos_alumno(alumno)


def actualizar_nota(alumnos: list[dict]) -> None:
    """Solicita un DNI y modifica la nota del alumno encontrado.

    Args:
        alumnos: Lista de alumnos donde se realizará la modificación.

    Returns:
        None: No retorna ningún valor.
    """
    print("\n" + "=" * 48)
    print("              MODIFICAR NOTA")
    print("=" * 48)

    dni = solicitar_dni()
    alumno = buscar_alumno(alumnos, dni)

    if alumno is None:
        print("\n  [AVISO] No se encontró un alumno con ese DNI.")
        print("-" * 48)
        return

    print("\n  Alumno seleccionado:")
    print(f"  Nombre: {alumno['nombre']} {alumno['apellido']}")
    print(f"  Nota actual: {alumno['nota']:g}")

    print("\n  Ingrese la nueva calificación:")
    nueva_nota = solicitar_nota()

    if modificar_nota(alumnos, dni, nueva_nota):
        print("\n" + "-" * 48)
        print("  [OK] Nota modificada correctamente.")
        print(f"  Nueva nota: {nueva_nota:g}")
        print("-" * 48)


def quitar_alumno(alumnos: list[dict]) -> None:
    """Solicita el DNI y elimina al alumno correspondiente.

    Args:
        alumnos: Lista de alumnos donde se realizará la eliminación.

    Returns:
        None: No retorna ningún valor.
    """
    print("\n" + "=" * 48)
    print("              ELIMINAR ALUMNO")
    print("=" * 48)

    dni = solicitar_dni()

    if eliminar_alumno(alumnos, dni):
        print("\n  [OK] Alumno eliminado correctamente.")
    else:
        print("\n  [AVISO] No se encontró un alumno con ese DNI.")

    print("-" * 48)


# --- FUNCIONES ESTADÍSTICAS ---

def mostrar_promedio(alumnos: list[dict]) -> None:
    """Calcula y muestra el promedio general de las notas.

    Args:
        alumnos: Lista de alumnos que se utilizará para el cálculo.

    Returns:
        None: No retorna ningún valor.
    """
    print("\n" + "=" * 48)
    print("             PROMEDIO GENERAL")
    print("=" * 48)

    promedio = calcular_promedio(alumnos)

    if promedio is None:
        print("\n  No hay alumnos registrados para calcular el promedio.")
    else:
        print(f"\n  Cantidad de alumnos: {len(alumnos)}")
        print(f"  Promedio general:   {promedio:.2f}")

    print("-" * 48)


def mostrar_mejor_nota(alumnos: list[dict]) -> None:
    """Muestra la calificación máxima y los alumnos correspondientes.

    Args:
        alumnos: Lista de alumnos que se utilizará para la consulta.

    Returns:
        None: No retorna ningún valor.
    """
    print("\n" + "=" * 48)
    print("                MEJOR NOTA")
    print("=" * 48)

    resultado = mejor_nota(alumnos)

    if resultado is None:
        print("\n  No hay alumnos registrados.")
        print("-" * 48)
        return

    nota_maxima, mejores_alumnos = resultado

    print(f"\n  Mejor calificación: {nota_maxima:g}")
    print("\n  Alumnos que obtuvieron esta nota:")

    for alumno in mejores_alumnos:
        print(f"  - {alumno['nombre']} {alumno['apellido']}")
        print(f"    DNI: {alumno['dni']}")

    print("-" * 48)


def mostrar_clasificacion(alumnos: list[dict]) -> None:
    """Muestra los alumnos aprobados y desaprobados.

    Args:
        alumnos: Lista de alumnos que se utilizará para la clasificación.

    Returns:
        None: No retorna ningún valor.
    """
    print("\n" + "=" * 48)
    print("       CLASIFICACIÓN DE ALUMNOS")
    print("=" * 48)
    print("  Criterio de aprobación: nota igual o mayor a 6.")
    print("-" * 48)

    aprobados, desaprobados = aprobados_desaprobados(alumnos)

    mostrar_lista_alumnos("ALUMNOS APROBADOS", aprobados)
    mostrar_lista_alumnos("ALUMNOS DESAPROBADOS", desaprobados)

    print("\n  RESUMEN")
    print(f"  Aprobados:     {len(aprobados)}")
    print(f"  Desaprobados:  {len(desaprobados)}")
    print(f"  Total:         {len(alumnos)}")
    print("-" * 48)


# --- PROGRAMA PRINCIPAL ---

def main() -> None:
    """Inicializa el sistema y controla el menú principal.

    Returns:
        None: No retorna ningún valor.
    """
    alumnos = []
    ejecutando = True

    while ejecutando:
        mostrar_menu()
        opcion = solicitar_opcion()

        if opcion == 1:
            cargar_alumno(alumnos)

        elif opcion == 2:
            mostrar_lista_alumnos(
                "LISTA DE ALUMNOS",
                listar_alumnos(alumnos)
            )

        elif opcion == 3:
            consultar_alumno(alumnos)

        elif opcion == 4:
            actualizar_nota(alumnos)

        elif opcion == 5:
            quitar_alumno(alumnos)

        elif opcion == 6:
            mostrar_promedio(alumnos)

        elif opcion == 7:
            mostrar_mejor_nota(alumnos)

        elif opcion == 8:
            mostrar_clasificacion(alumnos)

        elif opcion == 9:
            print("\n" + "=" * 48)
            print("       GRACIAS POR UTILIZAR EL SISTEMA")
            print("=" * 48)
            ejecutando = False

        else:
            print("\n  [ERROR] Opción incorrecta.")
            print("  Seleccione una opción del 1 al 9.")


# --- INICIO DE EJECUCIÓN ---

if __name__ == "__main__":
    main()
