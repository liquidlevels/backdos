CREATE DATABASE IF NOT EXISTS inegi_emmanuel;
USE inegi_emmanuel;

CREATE TABLE IF NOT EXISTS establecimiento (
    establecimiento_pk INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    codigo_postal CHAR(5) NOT NULL DEFAULT '0',
    latitud DECIMAL(9, 6) NOT NULL, 
    longitud DECIMAL(9, 6) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS contactos (
    telefono JSON NOT NULL DEFAULT (JSON_ARRAY()),
    correo JSON NOT NULL DEFAULT (JSON_ARRAY()),
    web JSON NOT NULL DEFAULT (JSON_ARRAY()),
    contactos INT UNSIGNED DEFAULT 0, 
    establecimiento_id INT,
    FOREIGN KEY (establecimiento_id) REFERENCES establecimiento(establecimiento_pk)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS municipio (
    municipio_pk INT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS tipo_actividad (
    tipo_actividad_pk INT PRIMARY KEY,
    nombre varchar(255) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS tipo_vialidad (
    tipo_vialidad_pk INT PRIMARY KEY,
    nombre varchar(255) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS tipo_asentamiento (
    tipo_asentamiento_pk INT,
    nombre VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS localidad (
    localidad_pk INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS entidad (
    entidad_pk INT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
) ENGINE=InnoDB;


CREATE TABLE IF NOT EXISTS informacion_legal (
    razon_social VARCHAR(255) NOT NULL DEFAULT '0',
    tipo_establecimiento TINYINT NOT NULL,
    fecha_alta CHAR(7) NOT NULL,
    establecimiento_id INT,
    FOREIGN KEY (establecimiento_id) REFERENCES establecimiento(establecimiento_pk)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS direccion (
    nombre_vialidad VARCHAR(255) NOT NULL DEFAULT '0',
    numero_exterior VARCHAR(10) NOT NULL DEFAULT '0',
    nombre_asentamiento VARCHAR(255) NOT NULL,
    codigo_postal CHAR(5) DEFAULT '0',
    localidad varchar(255) NOT NULL,
    entidad_id INT,
    establecimiento_id INT,
    FOREIGN KEY (establecimiento_id) REFERENCES establecimiento(establecimiento_pk)
) ENGINE=InnoDB;
