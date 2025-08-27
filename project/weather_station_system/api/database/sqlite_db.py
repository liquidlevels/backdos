import sqlite3

def database_init():
    try:
        connection = sqlite3.connect('weather_station_test.db')
        cursor = connection.cursor()
        queries = []

        create_tower_identification = """
            CREATE TABLE tower_identification (
                tower_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,            
                location TEXT,
                assigned_user TEXT,
                status TEXT NOT NULL CHECK(
                status IN ('Active', 'Inactive', 'Failure', 'Maintenance'))
            )"""
        queries.append(create_tower_identification)

        create_weather_measurements = """
            CREATE TABLE weather_measurements (
                tower_id TEXT PRIMARY KEY,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                temperature FLOAT,
                relative_humidity FLOAT,
                atmospheric_pressure FLOAT,
                wind_speed FLOAT,
                wind_direction INTEGER,
                precipitation FLOAT,
                solar_radiation FLOAT,
                uv_index INTEGER
            )"""
        queries.append(create_weather_measurements)

        create_tower_diagnostics = """
            CREATE TABLE tower_diagnostics (
                tower_id TEXT NOT NULL,
                battery_level REAL,
                last_connection_time DATETIME NOT NULL,
                temperature_sensor_status TEXT NOT NULL CHECK(temperature_sensor_status IN ('OK', 'Error')),
                humidity_sensor_status TEXT NOT NULL CHECK(humidity_sensor_status IN ('OK', 'Error')),
                overall_status TEXT NOT NULL CHECK(overall_status IN ('Normal', 'Warning', 'Critical')),
                FOREIGN KEY (tower_id) REFERENCES tower_identification(tower_id)
            )"""
        queries.append(create_tower_diagnostics)

        create_administrative_data = """
            CREATE TABLE tower_administration (
                admin_id TEXT PRIMARY KEY,
                tower_id TEXT NOT NULL,
                creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                last_update DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                notes TEXT DEFAULT NULL,
                data_source TEXT NOT NULL CHECK(data_source IN ('Simulator', 'Excel', 'Manual')),
                FOREIGN KEY (tower_id) REFERENCES tower_identification(tower_id)
            )"""
        queries.append(create_administrative_data)

        list_length = len(queries)
        for i in range(0, list_length):
            cursor.execute(queries[i])

        connection.commit()
        queries.clear()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

def insert_weather_measurements(data):
    try:
        connection = sqlite3.connect('weather_station.db')
        cursor = connection.cursor()

        query = """
            INSERT INTO weather_measurements (
                temperature, 
                relative_humidity, 
                atmospheric_pressure, 
                wind_speed, 
                wind_direction, 
                precipitation, 
                solar_radiation, 
                uv_index
            ) VALUES (?,?,?,?,?,?,?,?)
        """

        cursor.execute(query,(
            data["temperature"],
            data["relative_humidity"],
            data["atmospheric_pressure"],
            data["wind_speed"],
            data["wind_direction"],
            data["precipitation"],
            data["solar_radiation"],
            data["uv_index"]
        ))

        connection.commit()
    
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()
