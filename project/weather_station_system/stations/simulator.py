import json
import random
import time
from datetime import datetime
from sqlite_data import insert_weather_measurements

def generate_data():
    return {
        "temperature": round(random.uniform(10, 35)),  # °C
        "relative_humidity": round(random.uniform(30, 95)),  # %
        "atmospheric_pressure": round(random.uniform(980, 1040)),  # hPa
        "wind_speed": round(random.uniform(0, 25), 1),  # m/s
        "wind_direction": random.randint(0, 360),  # grados
        "precipitation": round(random.uniform(0, 10), 1),  # mm/h
        "solar_radiation": round(random.uniform(0, 1200)),  # W/m²
        "uv_index": random.randint(0, 11),  # índice UV
    }

def simulate_weather_station(time_interval):
    try:
        while True:
            data = generate_data()
            json_data = json.dumps(data, indent=2)
            print(f"\nSimulated data ({datetime.now().strftime('%d-%m-%Y %H:%M:%S')}):")
            insert_weather_measurements(data)
            
            time.sleep(time_interval)
            
    except KeyboardInterrupt:
        print("\nSimulation stopped by user")

if __name__ == "__main__":
    simulate_weather_station(time_interval=2)
