#! usr/bin/env python3

# REALIZANDO UN CAMBIO PARA PROBAR GIT

#realizando más cambios , v6, esta vez modificando más abajo también
#probando nuevamente v7 porque perdi los cambios anteriores
#luego de hacer git rm --cached [filename]
#v9 removí el seguimiento de todos los archivos seguidos. Intenté un checkout de versión anterior y no funcionó



import sqlite3

#Generar BBDD temporal en memoria
conexion=sqlite3.connect(':memory:')

#Generar elemento de la clase cursor vinculado a la conexión
cursor=conexion.cursor()

#Crear tabla en BBDD
cursor.execute("""
CREATE TABLE IF NOT EXISTS ventas(
id INTEGER PRIMARY KEY AUTOINCREMENT,
articulo TEXT NOT NULL,
precio REAL,
cantidad INTEGER)
""")

#Generar las tuplas que serán cargadas en la BBDD
tupla1=("peras", 10.5, 4)
tupla2=("manzanas", 2.5, 4)
tupla3=("duraznos", 5.5, 7)
tupla4=("peras", 10, 3)

#Cargar datos en BBDD (probando)
cursor.execute("""
INSERT INTO ventas(articulo, precio, cantidad)
VALUES (?,?,?)
""", tupla1)

cursor.execute("""
INSERT INTO ventas(articulo, precio, cantidad)
VALUES (?, ?, ?)
""", tupla2)

cursor.execute("""
INSERT INTO ventas(articulo, precio, cantidad)
VALUES (?, ?, ?)
""", tupla3)

cursor.execute("""
INSERT INTO ventas(articulo, precio, cantidad)
VALUES (?, ?, ?)
""", tupla4)




def listar_todos():
    #Obtener valores de la BBDD
    cursor.execute("""
    SELECT * FROM ventas
    """)
    #Traer resultados de la query
    rows=cursor.fetchall()

    #Imprimir query
    for row in rows:
        print(row)

def listar_articulos(art):
    #Recuperar consulta especifica
    cursor.execute("""
        SELECT articulo, cantidad FROM ventas WHERE articulo=?
    """, (art,) )

    #Traer resultados de la query
    rows=cursor.fetchall()

    #Imprimir query
    if len(rows)>0:
        for row in rows:
           print(row)
    else:
        print("No se encontraron elementos con el criterio indicado")

def sumarizar_articulos(art):
    #Recuperar consulta especifica
    cursor.execute("""
        SELECT articulo, SUM(cantidad) FROM ventas WHERE articulo=?
    """, (art,) )

    #Traer resultados de la query

    rows=cursor.fetchall()

    #Imprimir query
    if len(rows)>0:
        for row in rows:
           print(row)
    else:
        print("No se encontraron elementos con el criterio indicado")


palabra=input("Ingrese articulo a buscar: ")

print("\n***** Listar articulos que coincidan con la palabra: " + palabra)
listar_articulos(palabra)

print("\n***** Sumarizar articulos que coincidan con la palabra: " + palabra)
sumarizar_articulos(palabra)

print("\n***** Listar todos")
listar_todos()

conexion.close()

#EOF
