import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# make time axis
start = datetime.now()
times = [start + timedelta(minutes=i) for i in range(1440)]

# generate sensor data
temp = 22 + np.sin(np.linspace(0, 4*np.pi, 1440)) * 3 + np.random.normal(0, 0.2, 1440)
humidity = 55 + np.cos(np.linspace(0, 4*np.pi, 1440)) * 5 + np.random.normal(0, 0.5, 1440)

# put into DataFrame
df = pd.DataFrame({
    "time": times,
    "temperature_C": temp,
    "humidity_percent": humidity
})

plt.figure(figsize=(10,5))
plt.plot(df["time"], df["temperature_C"], label="Temperature (C)")
plt.plot(df["time"], df["humidity_percent"], label="Humidity (%)")
plt.xlabel("Time")
plt.ylabel("Sensor Reading")
plt.title("Simulated Environmental Sensor Data")
plt.legend()
plt.tight_layout()

import os
output_path = os.path.join(os.path.dirname(__file__), "sensor_plot.png")
plt.savefig(output_path)

plt.show()


print("Average temperature:", df["temperature_C"].mean())
print("Average humidity:", df["humidity_percent"].mean())