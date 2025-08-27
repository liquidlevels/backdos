from dataclasses import dataclass
from datetime import datetime

@dataclass
class TowerIdentification:
    tower_id: string
    name: string
    location: string
    assigned_user: string
    status: string

@dataclass
class WeatherMeasurement:
    temperature: float
    relative_humidity: float
    atmospheric_pressure: float
    wind_speed: float
    wind_direction: int
    precipitation: float
    solar_radiation: float
    uv_index: int

@dataclass
class TowerDiagnostics:
    tower_id: string
    battery_level: float
    last_connection_time: datetime
    temperature_sensor_status: string
    overall_status: string

@dataclass
class AdministrativeData:
    admin_id: string
    tower_id: string
    creation_date: datetime
    last_update: datetime
    notes: string
    data_source: text
