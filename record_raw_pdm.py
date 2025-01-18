import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import decimate
from scipy.io.wavfile import write
import time

import argparse

parser = argparse.ArgumentParser(description="Record PDM data from serial input.")
parser.add_argument(
    "--file_name",
    type=str,
    required=True
)

args = parser.parse_args()
file_name = f"{args.file_name}.txt"

# Initialize Serial Port
ser = serial.Serial('COM5', 2000000, timeout=1)  # Adjust COM port as needed
print("Serial connection established.")
plt.ion()
# Set up for PDM-to-PCM conversion
pdm_clock_rate = 2000000  # 1 MHz PDM clock

# Recording duration setup
recording_duration = 5  # seconds
# total_samples_needed = pdm_clock_rate * recording_duration  # Total PDM samples required
pdm_data = []
print(f"Starting 5-second recording...")
Recording_start = False
# Collect PDM data for 5 seconds
start_time = time.time()
current_time = time.time()
while (current_time - start_time) <= recording_duration :
    try:
        value = int(ser.readline().decode().strip())
        if Recording_start == False:
            start_time = time.time()
            Recording_start = True
        pdm_data.append(value)
        current_time = time.time()
    except ValueError:
        continue
end_time = current_time
print(f"Recording complete in {end_time - start_time:.2f} seconds")

# Save PDM data to a .txt file
with open(file_name, 'w') as file:
    for item in pdm_data:
        file.write(f"{item}\n")
print(f"Data saved to {file_name}")