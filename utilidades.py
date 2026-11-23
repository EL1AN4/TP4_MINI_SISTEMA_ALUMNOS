
"""
Módulo de utilidades y validaciones.

Contiene funciones auxiliares para solicitar información al usuario
y validar los datos ingresados antes de utilizarlos en el sistema.
"""


# --- VALIDACIONES DE ENTRADA ---

def solicitar_texto(mensaje: str) -> str:
    """Solicita un texto y evita que el campo quede vacío.

    Args:
        mensaje: Texto que se mostrará al solicitar la información.

    Returns:
        str: Texto ingresado y sin espacios externos.
    """
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("  [ERROR] El campo no puede estar vacío.")


def solicitar_dni() -> str:
    """Solicita un DNI compuesto únicamente por números.

    Returns:
        str: Número de documento ingresado por el usuario.
    """
    while True:
        dni = input("  DNI: ").strip()

        if dni.isdigit():
            return dni

        print("  [ERROR] El DNI debe contener solamente números.")


def solicitar_nota() -> float:
    """Solicita una nota numérica dentro del rango permitido.

    Returns:
        float: Calificación ingresada, comprendida entre 0 y 10.

    Raises:
        No propaga ValueError, ya que controla internamente los errores
        de conversión mediante try/except.
    """
    while True:
        try:
            nota = float(input("  Nota (0 a 10): "))

            if 0 <= nota <= 10:
                return nota

            print("  [ERROR] La nota debe estar entre 0 y 10.")

        except ValueError:
            print("  [ERROR] Ingrese un valor numérico válido.")


def solicitar_opcion() -> int:
    """Solicita una opción numérica para el menú principal.

    Returns:
        int: Opción ingresada o 0 si el valor no es un número entero.

    Raises:
        No propaga ValueError, ya que controla internamente los errores
        de conversión mediante try/except.
    """
    try:
        return int(input("\n  Seleccione una opción: "))

    except ValueError:
        print("\n  [ERROR] Ingrese una opción numérica válida.")
        return 0
