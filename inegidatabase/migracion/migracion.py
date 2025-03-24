import csv
import mysql.connector
from mysql.connector import Error

def connect_to_database(user, password, host, database):
    config = {
        'user': user,
        'password': password,
        'host': host,
        'port': '3306',
        'database': database
    }

    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_data(connection, query, csv_file):
    data = []
    cursor = connection.cursor()

    with open(csv_file, mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)
            data.append(tuple(lines))

    cursor.executemany(query, data)
    connection.commit()

    
if __name__ == "__main__":
    establecimiento = """
        INSERT INTO establecimiento (
            establecimiento_pk,
            nombre, 
            codigo_postal, 
            latitud, 
            longitud) 
        VALUES (%s,%s,%s,%s,%s)
    """

    contactos = """
        INSERT INTO contactos (
            telefono, 
            correo, 
            web, 
            contactos, 
            establecimiento_id)
        VALUES (%s,%s,%s,%s,%s)
    """

    municipio = "INSERT INTO municipio (municipio_pk, nombre) VALUES (%s,%s)"

    tipo_actividad = "INSERT INTO tipo_actividad (tipo_actividad_pk, nombre) VALUES (%s,%s)"

    tipo_vialidad = "INSERT INTO tipo_vialidad (tipo_vialidad_pk, nombre) VALUES (%s,%s)"

    tipo_asentamiento = "INSERT INTO tipo_asentamiento (tipo_asentamiento_pk, nombre) VALUES (%s,%s)"

    entidad = "INSERT INTO entidad (entidad_pk, nombre) VALUES (%s,%s)"

    informacion_legal = """
        INSERT INTO informacion_legal (
            razon_social,
            tipo_establecimiento,
            fecha_alta,
            establecimiento_id
        )
        VALUES (%s,%s,%s,%s)
    """

    direccion = """
        INSERT INTO direccion (
            nombre_vialidad, 
            numero_exterior, 
            nombre_asentamiento, 
            codigo_postal, 
            localidad, 
            entidad_id,
            establecimiento_id
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    queries = [establecimiento, contactos, municipio, tipo_actividad, tipo_vialidad, tipo_asentamiento, entidad, informacion_legal, direccion]
    files = ['establecimientos.csv', 'contactos.csv', 'municipio.csv', 'actividad.csv', 'vialidad.csv', 'asentamiento.csv', 'entidad.csv', 'informacion_legal.csv', 'direccion.csv']

    conn = connect_to_database('user', 'password', 'localhost', 'database')
    if conn:
        list_length = len(queries)
        for i in range (0, list_length):
            insert_data(conn, queries[i], files[i])
        conn.close()
