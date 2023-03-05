import psycopg2
import json

# Especificar los detalles de la conexión a la base de datos
username = 'rami'
password = 'rami'
database = 'rami'
hostname = 'localhost'
port = 5432

# Conectarse a la base de datos utilizando psycopg2
conn = psycopg2.connect(
    dbname=database,
    user=username,
    password=password,
    host=hostname,
    port=port
)

# Crear un cursor
cur = conn.cursor()

# Ejecutar una consulta
cur.execute("SELECT id_user, name, lastname, password FROM users")

# Obtener los resultados de la consulta
results = cur.fetchall()

# Convertir los resultados en una cadena JSON
json_results = json.dumps(results)

# Imprimir los resultados

print(json_results)

# Cerrar el cursor y la conexión
cur.close()
conn.close()
