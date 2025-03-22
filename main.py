import openpyxl

# PARTE 1: Crear diccionario y entrada de datos
# Crea un diccionario vacío llamado 'estudiantes'
# Usa un ciclo for para pedir 3 nombres y notas (convierte la nota a float)
# Guarda cada par nombre-nota en el diccionario
# --- Escribe tu código aquí ---
estudiantes = {} # type: ignore

for x in range(3):
    nombre = input("Ingesa el nombre del estudiante: ")
    nota = float(input(f"Ingresa la anota del {nombre}: "))
    estudiantes[nombre] = nota



# PARTE 2: Crear archivo Excel
# Crea un nuevo libro de trabajo con openpyxl.Workbook()
libro = openpyxl.Workbook()
# Obtén la hoja activa
hoja = libro.active

# PARTE 3: Escribir encabezados
# Escribe "Estudiante" en A1 y "Nota" en B1
# --- Escribe tu código aquí ---
hoja["A1"]= "Estudiante"
hoja["B1"]= "Nota"


# PARTE 4: Escribir datos con ciclo
# Usa un ciclo for para recorrer el diccionario
# Escribe el nombre en la columna A y la nota en la columna B
# Incrementa 'fila' en cada iteración
# --- Escribe tu código aquí ---
fila = 2
for nombre, nota in estudiantes.items():
    hoja[f"A{fila}"] = nombre
    hoja[f"B{fila}"] = nota
    fila+=1


# PARTE 5: Guardar archivo
# Guarda el archivo como "ejercicio1.xlsx"
# --- Escribe tu código aquí ---
libro.save(("ejercicio1.xlsx"))
print("¡Ejercicio 1 guardado en ejercicio1.xlsx!")