# Normalizacion
Documentacion de normalizacion de base de datos obtenida de [Inegi](https://www.inegi.org.mx/contenidos/masiva/denue/denue_02_csv.zip).

## Datos originales

| id       | clee                          | nom_estab                                 | raz_social                                   | codigo_act | nombre_act                                                     | per_ocu           | tipo_vial      | nom_vial                 | tipo_v_e_1       | nom_v_e_1                     | tipo_v_e_2      | nom_v_e_2           | tipo_v_e_3      | nom_v_e_3             | numero_ext | letra_ext | edificio  | edificio_e | numero_int | letra_int | tipo_asent      | nomb_asent                                    | tipoCenCom | nom_CenCom | num_local | cod_postal | cve_ent | entidad         | cve_mun | municipio | cve_loc | localidad                                    | ageb  | manzana | telefono     | correoelec                          | www                            | tipoUniEco | latitud      | longitud      | fecha_alta |
|---------|------------------------------|-----------------------------------------|-------------------------------------------|-----------|----------------------------------------------------------------|------------------|---------------|--------------------------|-----------------|--------------------------------|----------------|----------------|----------------|-----------------|------------|------------|-----------|------------|------------|------------|----------------|---------------------------------------------|------------|------------|-----------|------------|---------|----------------|---------|------------|---------|---------------------------------------------|------|---------|--------------|---------------------------------|--------------------------------|------------|--------------|--------------|------------|
| 8320509 | 02002115111000041000026891S5 | ABS PROMOTORA DE MEXICO                 | ABS PROMOTORA DE MEXICO SA DE CV          | 115111    | Servicios de fumigación agrícola                              | 0 a 5 personas  | CALLE         | NINGUNO                  | CALLE          | NINGUNO                        | CALLE         | NINGUNO        | CALLE         | NINGUNO         | 0          | SN         |           |            |            |            | EJIDO          | HERMOSILLO                                     |            |            |           | 21840      | 2       | Baja California | 2       | Mexicali   | 192     | Ejido Hermosillo                             | 8423  | 3       |              |                                 |                                | Fijo       | 32.52337876  | -114.917782  | 2019-11    |
| 8838283 | 02001112512000434000000000U6 | ABULONES CULTIVADOS                     | ABULONES CULTIVADOS S DE RL DE CV         | 112519    | Otra acuicultura                                           | 11 a 30 personas | CALLE         | MACHERO                  | CALLE          | TERCETA                        | CALLE         | CUARTA         | CALLE         | RIBEROL         | 366        | 11         | MAXICOM   | PISO 1     |            |            | COLONIA        | SECCIÓN PRIMERA                               |            |            |           |            | 2       | Baja California | 1       | Ensenada   | 1       | Ensenada                                     | 717   | 16      |              | JUANITA.ROMAN@ABULONES.MX      | WWW.ABULONESCULTIVADOS.COM    | Fijo       | 31.8621572   | -116.6267073 | 2019-11    |
| 6166487 | 02002112511000012001000000U0 | ACUICOLA TRIPLEA                        |                                           | 112514    | Camaronicultura y acuicultura de otros crustáceos en agua dulce | 6 a 10 personas  | OTRO(ESPECIFIQUE) | NINGUNO                  | OTRO(ESPECIFIQUE) | NINGUNO                        | OTRO(ESPECIFIQUE) | NINGUNO        | OTRO(ESPECIFIQUE) | NINGUNO         | 0          | DOMICILIO CONOCIDO |           |            |            |            | COLONIA        | VENUSTIANO CARRANZA                          |            |            |           |            | 2       | Baja California | 2       | Mexicali   | 1581    | Los Ángulos (Colonia Venustiano Carranza)    | 3653  | 800     |              | NORITA95@LIVE.COM              |                                | Fijo       | 32.20725336  | -115.1462315 | 2010-07    |
| 8346295 | 02001115113000137000000000U9 | AGRICOLA DOS MARES                      | AGRICOLA DOS MARES SC DE RL               | 115113    | Beneficio de productos agrícolas                          | 51 a 100 personas | CALLE         | SINALOA                  | CALLE          | RODOLFO SÁNCHEZ TABOADA        | CALLE         | BENITO JUÁREZ  | AVENIDA       | 19 DE MARZO    | 0          | SN         |           |            |            |            | EJIDO          | PUNTA COLNETT (PUNTA COLONET)                 |            |            |           |            | 2       | Baja California | 1       | Ensenada   | 186     | Ejido Punta Colnett (Punta Colonet)          | 9956  | 4       | 6462109444   | RHUMANOS@2MARES.COM.MX         |                                | Fijo       | 31.06657818  | -116.2098943 | 2019-11    |
| 9323240 | 02002115113000031000000000U2 | AGRICOLA LAS MONTAÑAS                   | AGRICOLA LAS MONTAÑAS SA DE CV            | 115113    | Beneficio de productos agrícolas                          | 0 a 5 personas   | CARRETERA     | A BATAQUES MURGUIA       |                 |                                |                |                |                |                 | 0          | SN         |           |            | 0          | KM 17.5    | COLONIA        | CHAPULTEPEC                                    |            |            |           |            | 2       | Baja California | 2       | Mexicali   | 2900    | Familia Lamarque (Colonia Chapultepec)       | 362A  | 800     |              | NMARTINEZ@ALM.COM.MX           |                                | Fijo       | 32.3266025   | -115.0714433 | 2020-11    |
| 6166344 | 02001114119001542001000000U7 | AGROMARISMA                             | AGROMARISMA                                | 114119    | Pesca y captura de peces, crustáceos, moluscos y otras especies | 6 a 10 personas  | CALLE         | ITURBIDE                 | CALLE          | SEGUNDA                        | CALLE         | TERCERA        | CALLE         | RAYON           | 284        |            | 3         |            |            |            | COLONIA        | OBRERA                                        |            |            |           | 22890      | 2       | Baja California | 1       | Ensenada   | 1       | Ensenada                                     | 076A  | 6       |              | WWW.AGROMARISMA@HOTMAIL.COM    |                                | Fijo       | 31.86168362  | -116.6113703 | 2010-07    |


## Columnas eliminadas

En esta seccion se explica de manera general el por que y cuales fueron las columnas que se eliminaron 


---
- tipo_v_e_1
- nom_v_e_1
- tipo_v_e_2
- nom_v_e_2
- tipo_v_e_3
- nom_v_e_3

Estos datos se descartan porque en la aplicacion no se necesitan las entre calles del establecimiento.

---

- letra_ext
- numero_int
- letra_int
- tipoCenCom
- nom_CenCom
- num_local
- edificio
- edificio_e

Estos datos han sido descartados debido a que muy pocos establecimientos los han proporcionado, ademas de ser poco relevantes.

---
- clee
- ageb
- manzana

Estos datos son poco relevantes debido a que no les damos un determinado uso.

---


## Tablas creadas

Con las columnas restantes, se crearon un total de nueve tablas, de las cuales tres es donde yace la principal fuente de informacion sobre los establecimientos, siendo *Establecimiento* la principal de estas, seguido de *Contactos* y *Direccion*. Las seis tablas restantes son diccionarios los cuales ayudan a tener un mejor manejo de la informacion.

### Principales
Establecimiento

| ID      | Nombre Establecimiento      | Código Postal | Latitud      | Longitud      | Ubicación                    |
|---------|-----------------------------|--------------|-------------|--------------|------------------------------|
| 8320509 | ABS PROMOTORA DE MEXICO     | 21840        | 32.52337876  | -114.917782  | -114.91778195 32.52337876    |
| 8838283 | ABULONES CULTIVADOS         | 0            | 31.8621572   | -116.6267073 | -116.6267073 31.8621572      |

Contactos

| Telefono  | Email                           | Web                               | Contactos | ID_establecimiento       |
|-----|---------------------------------|----------------------------------|--------|----------|
| {}  | {}                              | {}                               | 0      | 8320509  |
| {}  | JUANITA.ROMAN@ABULONES.MX       | WWW.ABULONESCULTIVADOS.COM       | 6      | 8838283  |

Direccion

| ID      | Nombre Vial | Número Exterior | Nombre Asentamiento | Código Postal | Localidad         | ID Entidad |
|---------|------------|----------------|---------------------|--------------|-------------------|------------|
| 8320509 | NINGUNO    | 0              | HERMOSILLO          | 21840        | Ejido Hermosillo  | 2          |
| 8838283 | MACHERO    | 366            | SECCIÓN PRIMERA     | 0            | Ensenada          | 2          |

Informacion Legal

| razon_social                          | tipo_establecimiento | fecha_alta | establecimiento_id |
|---------------------------------------|----------------------|------------|--------------------|
| ABS PROMOTORA DE MEXICO SA DE CV      | 1                    | 2019-11    | 8320509            |
| ABULONES CULTIVADOS S DE RL DE CV     | 1                    | 2019-11    | 8838283            |



### Diccionarios
Municipio

| ID  | nombre           |
|----:|----------------------|
|  1  | Ensenada            |
|  2  | Mexicali            |

Tipo_actividad
| ID   | nombre                          |
|----------|------------------------------------|
| 115111   | Servicios de fumigación agrícola  |
| 112519   | Otra acuicultura                  |

Tipo_vialidad

| ID | tipo_vialidad         |
|----|--------------------------|
| 1  | CALLE                   |
| 2  | OTRO(ESPECIFIQUE)        |

Tipo_asentamiento
| ID | tipo_asentamiento |
|----|----------------------|
| 1  | EJIDO               |
| 2  | COLONIA             |

Localidad
| ID | Localidad               |
|----|-------------------------|
| 15 | Los Hermanos           |
| 16 | Brisamar [Campo]       |

Entidad
| ID | Entidad         |
|----|--------------|
| 2  | Baja California |
