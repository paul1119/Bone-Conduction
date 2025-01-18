import serial
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import decimate, butter, lfilter
# Initialize Serial Port
ser = serial.Serial('COM5', 2000000, timeout=1)  # Adjust COM port as needed
print("Serial connection established.")
plt.ion()
# Set up for PDM-to-PCM conversion
pdm_clock_rate = 2000000 # 1MHz PDM clock
sampling_rate = 16000  # Target PCM sampling rate
decimation_factor = int (pdm_clock_rate // sampling_rate) # Adjusted decimation factor
# Prepare plot with dynamic length adjustment
fig, ax = plt.subplots()
data_points = 32768
x_data = list(range(data_points))

y_data = [0] * data_points
line, = ax.plot(x_data, y_data)
ax.set_ylim(-2, 2)
def pdm_to_pcm(pdm_signal, decimation_factor):
    """Convert PDM (1s and 0s) to PCM using decimation."""
    pdm_signal = np.array(pdm_signal) * 2 - 1  # Convert to -1 and +1
    pcm_signal = decimate(pdm_signal, decimation_factor, zero_phase=True)
    return pcm_signal

def update_plot(pcm_signal):
    """Update the plot with the new PCM data and handle size dynamically."""
    global x_data, y_data, line
    x_data = list(range(len(pcm_signal)))  # Adjust x-axis size to match PCM data
    line.set_xdata(x_data)
    line.set_ydata(pcm_signal)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.001)

# Function to apply a low-pass filter cutoff 5k
def low_pass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y



# Collect and convert PDM data in real-time
try:
    while True:
        pdm_data = []
        for _ in range(data_points):
            try:
                value = int(ser.readline().decode().strip())
                pdm_data.append(value)
            except ValueError:
                continue
        # Convert PDM to PCM and plot
        if len(pdm_data) > 0:
            pcm_data = pdm_to_pcm(pdm_data, decimation_factor)
            # Apply low-pass filter to PCM data
            cutoff_frequency = 2000  # Cutoff frequency for the low-pass filter
            print(len(pcm_data))
            filtered_pcm_data = low_pass_filter(pcm_data, cutoff_frequency, sampling_rate)
            # print(len(filtered_pcm_data))
            update_plot(filtered_pcm_data)
            # update_plot(pcm_data)

except KeyboardInterrupt:
    print("Stopped by user.")
    ser.close()
    plt.close()