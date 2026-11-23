# Mini Sistema de Alumnos en Memoria

Este proyecto consiste en un sistema de gestión de alumnos desarrollado en Python. Permite registrar, consultar, modificar y eliminar información de estudiantes mediante una lista de diccionarios.

Está pensado como un trabajo práctico para aplicar conocimientos sobre estructuras de datos, funciones, validaciones, operaciones CRUD y organización modular del código.

Los datos se almacenan en memoria durante la ejecución del programa, sin utilizar bases de datos ni archivos externos.

## Características

- **Cargar alumnos:** permite registrar estudiantes con DNI, nombre, apellido, curso y nota, evitando DNI duplicados.
- **Listar alumnos:** muestra todos los estudiantes registrados con sus respectivos datos.
- **Buscar alumno por DNI:** permite localizar un estudiante mediante su número de documento.
- **Modificar nota:** permite actualizar la calificación de un alumno registrado.
- **Eliminar alumno:** permite eliminar un estudiante de la lista mediante su DNI.
- **Calcular promedio general:** calcula el promedio de las notas de todos los alumnos registrados.
- **Mostrar mejor nota:** identifica la calificación más alta y los estudiantes que la obtuvieron.
- **Mostrar aprobados y desaprobados:** clasifica a los alumnos según su nota, considerando aprobado a quien obtiene 6 o más y desaprobado a quien obtiene menos de 6.

## Instalación

**Requisitos previos:**
- Python 3.10 o superior.
- Visual Studio Code.
- Git.
- Una cuenta de GitHub.

**Clonar el repositorio:**

```bash
git clone https://github.com/USUARIO/TP4_MINI_SISTEMA_ALUMNOS.git
cd TP4_MINI_SISTEMA_ALUMNOS
```

Reemplazar `USUARIO` por el nombre de usuario correspondiente de GitHub.

No es necesario instalar dependencias adicionales, ya que el proyecto utiliza exclusivamente módulos de Python estándar.

## Uso

Para ejecutar el sistema, abrir una terminal en la carpeta del proyecto y utilizar el siguiente comando:

```bash
python main.py
```

Una vez iniciado, se mostrará un menú interactivo con las siguientes opciones:

1. Cargar alumno.
2. Listar alumnos.
3. Buscar alumno por DNI.
4. Modificar nota.
5. Eliminar alumno por DNI.
6. Calcular promedio general.
7. Mostrar mejor nota.
8. Mostrar aprobados y desaprobados.
9. Salir.

Los datos permanecen disponibles mientras el programa está en ejecución. Al cerrarlo, la información registrada se pierde.

## Tecnologías

- **Python:** lenguaje de programación utilizado para desarrollar el sistema.
- **Visual Studio Code:** entorno de desarrollo utilizado para escribir y ejecutar el código.
- **Git:** sistema de control de versiones.
- **GitHub:** plataforma utilizada para alojar y gestionar el repositorio.

## Contribución

Se pueden reportar errores, sugerir mejoras o proponer modificaciones mediante la sección *Issues* del repositorio.

Para colaborar con el proyecto, se pueden enviar Pull Requests describiendo los cambios realizados y su finalidad.

## Licencia

Este proyecto está bajo la licencia MIT.


## Personas Desarrolladoras del Proyecto

- Giron Eliana.
