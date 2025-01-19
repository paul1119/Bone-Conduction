# Project Title

## Table of Contents
- [Introduction](#introduction)
- [Difference Between PDM and PCM Signals](#difference-between-pdm-and-pcm-signals)
- [Recording with recording_v1.ino on Arduino Uno](#recording-with-recording_v1.ino-on-arduino-uno)
- [Data Processing and Visualization](#data-processing-and-visualization)

## Introduction
For deeper explanation, you could go to proposal.pdf.<br/>
Current status, plot the received signal from BC_microphone. See images directory. 

## Difference Between PDM and PCM Signals
Pulse Density Modulation (PDM) and Pulse Code Modulation (PCM) are two different methods for digital representation of analog signals. PDM represents the signal as a density of pulses, with a high density indicating a high signal level and a low density indicating a low signal level. PCM, on the other hand, represents the signal as a series of numerical values that correspond to the amplitude of the signal at regular intervals. <br/>
1. https://users.ece.utexas.edu/~bevans/courses/realtime/lectures/10_Data_Conversion/AP_Understanding_PDM_Digital_Audio.pdf
2. https://tomverbeure.github.io/2020/10/04/PDM-Microphones-and-Sigma-Delta-Conversion.html

![image](https://github.com/user-attachments/assets/666d5aaf-0401-4e56-b428-0ad21703cf2d)

- **PDM (Pulse Density Modulation)**:
  - Encodes the signal by varying the density of pulses.
  - Used in applications like digital microphones.
  - Simpler hardware but requires higher processing power for decoding.

- **PCM (Pulse Code Modulation)**:
  - Encodes the signal by sampling the amplitude at regular intervals and quantizing it into a series of digital values.
  - Commonly used in audio and telecommunication systems.
  - More efficient for storage and transmission.

## Recording with recording_v1.ino on Arduino Uno
To record audio on the Arduino Uno, we use the `recording_v1.ino` script. This script initializes the microphone, reads the PDM data, and sends it over the serial port.

1. **Setup the Hardware**:
   - Connect the microphone to the Arduino Uno.
   - Ensure proper power supply and connections.

2. **Load the Script**:
   - Open the Arduino IDE and load `recording_v1.ino`.
   - Upload the script to the Arduino Uno board.

3. **Recording Process**:
   - The script reads the PDM data from the microphone.
   - It then sends the data over the serial port for further processing.

## Data Processing and Visualization
After obtaining the PDM data via serial, we use Python to process and visualize the data.

1. **Obtain Data**:
   - Connect the Arduino Uno to your computer.
   - Use a serial monitor to capture the incoming PDM data.
   - Use record_raw_pdm.py to record the output showed in serial.

2. **Processing with Python**:
   - Use Python scripts to read the PDM data.
   - Use plot_pdm_data.py to plot recorded data.
   - python plot_pdm_data.py --file_name test
   - Convert the PDM data to PCM format for easier analysis.

3. **Plotting Waveforms**:
   - Use libraries like Matplotlib to plot the PDM and PCM data.
   - Visualize the waveforms for analysis and verification.
