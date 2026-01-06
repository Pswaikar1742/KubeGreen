import time
import random
import sys

# Define a "Sensor" class - Good OOP practice
class EnergySensor:
    def __init__(self, location):
        self.location = location

    def get_reading(self):
        # Simulating wattage between 50W and 150W
        return round(random.uniform(50.0, 150.0), 2)

if __name__ == "__main__":
    print(f"Starting KubeGreen Sensor Node - {sys.platform}")
    sensor = EnergySensor("Lab-Unit-1")
    
    try:
        while True:
            power = sensor.get_reading()
            # Flush stdout so logs appear immediately in Docker later
            print(f"[{time.strftime('%H:%M:%S')}] Location: {sensor.location} | Power: {power} W", flush=True)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nShutting down sensor...")