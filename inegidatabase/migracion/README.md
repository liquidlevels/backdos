# Migracion

En este documento se explica que metodo se ha elegido para la migracion de la base de datos de Excel a MySQL.

Por fines practicos se ha optado por migrar los datos con ayuda de Python, mas concreto la libreria *mysql-connector-python* ya que con unas cuantas lineas de codigo se logra conectar y subir todos los datos de una manera sencilla.

## Preparacion del entorno

Para poder tener el entorno en el que se han hecho las pruebas se debe instalar lo siguiente: 

crea un entorno virtual de python
```
python3 -m venv venv
```

activa el entorno virtual de python
```
source venv/bin/activate
```

instala la libreria *version 9.2.9*

```
pip install mysql-connector-python
```

Una vez se ha preparado el entorno, se debe hacer una prueba con la conexion a MySQL. Para esto necesitamos previamente tener listo un entorno de MySQL, de lo contrario no se podra conectar. [Configurar entorno MySQL en Docker](https://github.com/liquidlevels/backenduno/blob/main/mysql.md) 


## Proceso de migracion

Primeramente en MySQL se debe crear la base de datos y las tablas de esta con [create.sql](https://github.com/liquidlevels/backdos/blob/main/inegidatabase/migracion/create.sql)

Una vez se tenga la base de datos, procede a ejecutar el codigo de Python [migracion.py](https://github.com/liquidlevels/backdos/blob/main/inegidatabase/migracion/migracion.py)

### Explicacion del codigo

Para tener una mejor gestion de insersion a tablas, se guardan los queries en variables como en el ejemplo a continuacion.

```
establecimiento = """
        INSERT INTO establecimiento (
            establecimiento_pk,
            nombre, 
            codigo_postal, 
            latitud, 
            longitud) 
        VALUES (%s,%s,%s,%s,%s)
    """
```


Esta funcion toma la informacion de un archivo *csv* dado, divide cada linea en *tuplas* y las almacena en una lista, con esto se logra hacer un query donde se insertan los 138,123 registros.
```
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
```

En un principio se cambiaban los parametros de la funcion a mano, despues se opto por hacer un ciclo for ejecutando la funcion en cada iteracion y como parametros se usan con valores obtenidos de listas con nombre del query y archivo csv de cada tabla.

```
queries = [establecimiento, contactos, municipio, tipo_actividad, tipo_vialidad, tipo_asentamiento, entidad, informacion_legal, direccion]
files = ['establecimientos.csv', 'contactos.csv', 'municipio.csv', 'actividad.csv', 'vialidad.csv', 'asentamiento.csv', 'entidad.csv', 'informacion_legal.csv', 'direccion.csv']

conn = connect_to_database('user', 'password', 'localhost', 'database')
    if conn:
        list_length = len(queries)
        for i in range (0, list_length):
            insert_data(conn, queries[i], files[i])
        conn.close()
```
