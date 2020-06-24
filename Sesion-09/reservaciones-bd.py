import sqlite3
import reservacion

# 1. Conectarse a la BD SQlite3, driver, framework, orm (object relational model, Django)
nom_bd = "reservaciones.sqlite3"  # productos, biblioteca, tienda
conn = sqlite3.connect(nom_bd)
cur = conn.cursor()  # indice de la BD

# 2. Crear tabla de Producto
sql = "DROP TABLE IF EXISTS Servicio"
cur.execute(sql)
sql = """
CREATE TABLE Servicio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_reservacion INTEGER,
    concepto VARCHAR(80),
    cantidad INTEGER,
    precio FLOAT
)
"""
cur.execute(sql)

# 3. Obtener data del archivo
nom_csv = "reservaciones.csv"
servicios = reservacion.lee_csv(nom_csv)

# 3. Insertar datos
# sql = """INSERT INTO Servicio VALUES (
#     null, {}, {}, {}, {})""".format()
# no usar porque puede ser suceptible de ser hackeado
for servicio in servicios:
    sql = """INSERT INTO Servicio VALUES (null, ?, ?, ?, ?)"""
    cur.execute(sql,
        (servicio.id,
         servicio.concepto,
         servicio.cantidad,
         servicio.precio)
    )
conn.commit()  # confirmar el guardado de datos

# 4. Consulta de datos
sql = "SELECT * FROM Servicio"
cur.execute(sql)
resultados = cur.fetchall()
for r in resultados:
    print(r)
    
# 5. consulta de una sóla reservación
print()
sql = "SELECT * FROM Servicio WHERE id_reservacion=3"
cur.execute(sql)
resultados = cur.fetchall()
for r in resultados:
    print(r)


# N. Cerrar la BD
conn.close()