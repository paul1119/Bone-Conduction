"""
import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import decimate
from scipy.io.wavfile import write
import time
# Initialize Serial Port
ser = serial.Serial('COM5', 115200, timeout=1)  # Adjust COM port as needed
print("Serial connection established.")
plt.ion()

pdm_data = []
print(f"Starting 5-second recording...")
Recording_start = False
# Collect PDM data for 5 seconds
start_time = time.time()
current_time = time.time()
while (current_time - start_time) <= 8 :
    current_time = time.time()
    try:
        value = int(ser.readline().decode().strip())
        pdm_data.append(value)
    except ValueError:
        continue

# Save PDM data to a .txt file
with open('pdm_data.txt', 'w') as file:
    for item in pdm_data:
        file.write(f"{item}\n")
print("Data saved to pdm_data.txt")
"""
# Read PDM data from the .txt file
with open('pdm_data.txt', 'r') as file:
    pdm_data = [int(line.strip()) for line in file]

print(len(pdm_data))
print(pdm_data[:10])