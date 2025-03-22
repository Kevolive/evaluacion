Generar un Archivo Excel con Notas de Estudiantes

Este script en Python solicita al usuario tres nombres de estudiantes junto con sus respectivas notas, almacena los datos en un diccionario y los guarda en un archivo Excel utilizando la biblioteca openpyxl.

Requisitos Previos

Antes de ejecutar el script, asegúrate de tener instalado openpyxl. Si no lo tienes, instálalo con:
pip install openpyxl

Funcionamiento del Script

Solicita al usuario tres nombres de estudiantes y sus respectivas notas.
Almacena los datos en un diccionario donde las claves son los nombres y los valores son las notas.
Crea un archivo Excel con una hoja de trabajo activa.

Escribe los datos en la hoja de cálculo:

La columna A contendrá los nombres de los estudiantes.
La columna B contendrá sus notas.
Guarda el archivo con el nombre ejercicio1.xlsx en el directorio actual.

Cómo Ejecutar el Script

Ejecuta el script en la terminal o en un entorno de desarrollo con:
python main.py

Estructura del Archivo Excel

El archivo generado tendrá la estructur donde muestre el nombre del estrudiante. y en la siguiente fila
muestre su respectiva nota. Por ejemplo: En la columna estudiantes aparece el nombre "Kevin". En la siguiente colunma, notas, apparece la nota "4.5".



Notas Adicionales

Si el script muestra un error de NameError: name 'estudiantes' is not defined, asegúrate de que la variable estudiantes = {} esté definida antes del bucle.

Si openpyxl está subrayado en tu editor, verifica que openpyxl esté instalado en el entorno virtual correcto.

Autor
Kevin Olivella
Este script fue desarrollado para fines educativos y prácticos en la manipulación de archivos Excel en Python.