import sqlite3

# 1. Conectarse a la BD SQlite3, driver, framework, orm (object relational model, Django)
nom_bd = "productos.sqlite3"  # productos, biblioteca, tienda
conn = sqlite3.connect(nom_bd)
cur = conn.cursor()  # indice de la BD

# 2. Crear tabla de Producto
sql = "DROP TABLE IF EXISTS Producto"
cur.execute(sql)
sql = """
CREATE TABLE Producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(80),
    cantidad INTEGER,
    precio FLOAT
)
"""
cur.execute(sql)

# 3. Insertar datos
sql = """INSERT INTO Producto VALUES (
    null, 'alimentos y bebidas', 1, 3000.00)"""
cur.execute(sql)
conn.commit()  # confirmar el guardado de datos
sql = """INSERT INTO Producto VALUES (
    null, 'transporte', 3, 600.00)"""
cur.execute(sql)
conn.commit()  # confirmar el guardado de datos

# 4. Consulta de datos
sql = "SELECT * FROM Producto"
cur.execute(sql)
resultados = cur.fetchall()
for r in resultados:
    print(r)


# N. Cerrar la BD
conn.close()