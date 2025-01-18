import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import decimate, butter, lfilter
import argparse
parser = argparse.ArgumentParser(description="Record PDM data from serial input.")
parser.add_argument(
    "--file_name",
    type=str,
    required=True
)

args = parser.parse_args()
file_name = f"{args.file_name}.txt"

# Function to convert PDM to PCM
def pdm_to_pcm(pdm_signal, decimation_factor):
    pdm_signal = np.array(pdm_signal) * 2 - 1  # Convert to -1 and +1
    pcm_signal = decimate(pdm_signal, decimation_factor, zero_phase=True)
    return pcm_signal

# Function to apply a low-pass filter
def low_pass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y

# Read PDM data from the .txt file
with open(file_name, 'r') as file:
    pdm_data = [int(line.strip()) for line in file]

# Adjust the PDM clock rate and target sampling rate
pdm_clock_rate = 2000000  # 4000 samples per second
sampling_rate = 16000  # Adjusted target PCM sampling rate to match PDM clock rate
decimation_factor = 200
# decimation_factor = int(pdm_clock_rate // sampling_rate)
if decimation_factor == 0:
    decimation_factor = 1  # Ensure the decimation factor is at least 1

# Convert PDM data to PCM
pcm_data = pdm_to_pcm(pdm_data, decimation_factor)

# Apply low-pass filter to PCM data
cutoff_frequency = 1000  # Cutoff frequency for the low-pass filter
filtered_pcm_data = low_pass_filter(pcm_data, cutoff_frequency, sampling_rate)

# Plot the filtered PCM data
plt.figure(figsize=(10, 5))
plt.plot(filtered_pcm_data)
plt.title('Filtered PCM Waveform')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

