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
# Set up for PDM-to-PCM conversion
pdm_clock_rate = 1000000  # 1 MHz PDM clock
target_pcm_rate = 44000  # Desired PCM sampling rate
decimation_factor = pdm_clock_rate // target_pcm_rate
# Prepare plot for after recording
fig, ax = plt.subplots()
ax.set_ylim(-1, 1)
def pdm_to_pcm(pdm_signal, decimation_factor):
    """Convert PDM (1s and 0s) to PCM using decimation."""
    pdm_signal = np.array(pdm_signal) * 2 - 1  # Convert 1/0 to ±1
    pcm_signal = decimate(pdm_signal, decimation_factor, zero_phase=True)
    return pcm_signal
# Recording duration setup
recording_duration = 5  # seconds
total_samples_needed = pdm_clock_rate * recording_duration  # Total PDM samples required
pdm_data = []
print(f"Starting 5-second recording...")
# Collect PDM data for 5 seconds
start_time = time.time()
while len(pdm_data) < total_samples_needed:
    try:
        value = int(ser.readline().decode().strip())
        pdm_data.append(value)
        print(value)
    except ValueError:
        continue
end_time = time.time()
print(f"Recording complete in {end_time - start_time:.2f} seconds")
# Convert collected PDM data to PCM
pcm_data = pdm_to_pcm(pdm_data, decimation_factor)
x_data = list(range(len(pcm_data)))
# Normalize the PCM data to 16-bit range
pcm_data_normalized = np.int16(pcm_data / np.max(np.abs(pcm_data)) * 32767)
# Save PCM data as a WAV file
wav_filename = "pdm_recording.wav"
write(wav_filename, target_pcm_rate, pcm_data_normalized)
print(f"WAV file saved as: {wav_filename}")
# Plot the recorded PCM data
ax.plot(x_data, pcm_data)
plt.title("5-Second PCM Recording")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.show()
# Close the serial connection
ser.close()
print("Serial connection closed.")