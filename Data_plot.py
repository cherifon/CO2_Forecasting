import serial
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from datetime import datetime
import threading
import time
import signal
import sys
import csv
import os
import re

# Serial port configuration
ser = serial.Serial('COM6', 115200, timeout=1)

# Initialize data lists
co2_data = []
temp_data = []
hum_data = []
time_data = []

# Create figure and subplots
fig = make_subplots(rows=3, cols=1, subplot_titles=('CO2', 'Temperature', 'Humidity'))

# Initialize traces
co2_trace = go.Scatter(x=[], y=[], mode='lines', name='CO2')
temp_trace = go.Scatter(x=[], y=[], mode='lines', name='Temperature')
hum_trace = go.Scatter(x=[], y=[], mode='lines', name='Humidity')

# Add traces to the figure
fig.append_trace(co2_trace, row=1, col=1)
fig.append_trace(temp_trace, row=2, col=1)
fig.append_trace(hum_trace, row=3, col=1)

# Update layout
fig.update_layout(title='Real-time Sensor Data',
                  xaxis_title='Time',
                  yaxis_title='Value')

# CSV file handling
csv_filename = 'sensor_data.csv'
csv_exists = os.path.exists(csv_filename)

# Function to handle CTRL+C stop
def signal_handler(sig, frame):
    print('\nStopping...')
    update_plot()
    ser.close()
    sys.exit(0)

# Set up signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Function to sanitize input data
def sanitize_input(data):
    sanitized_data = [re.sub(r'[^\d.-]', '', value) for value in data]
    return sanitized_data

# Function to read data from the serial port
def read_serial_data():
    global csv_is_empty
    while True:
        line = ser.readline().decode('utf-8').strip()
        #print(f"Received line: {line}")
        if line:
            data = line.split(',')
            if len(data) == 3:
                try:
                    data = sanitize_input(data)
                    co2, temp, hum = map(float, data)
                    time_now = datetime.now()

                    # Append data to lists
                    co2_data.append(co2)
                    temp_data.append(temp)
                    hum_data.append(hum)
                    time_data.append(time_now)

                    # Print values with timestamp to terminal
                    print(f"[{time_now.strftime('%Y-%m-%d %H:%M:%S')}] CO2: {co2} ppm, Temperature: {temp} °C, Humidity: {hum} %")

                    # Write data to CSV file
                    with open(csv_filename, 'a', newline='') as csv_file:
                        csv_writer = csv.writer(csv_file)
                        if not csv_exists or csv_is_empty:
                            csv_writer.writerow(['Timestamp', 'CO2 (ppm)', 'Temperature (°C)', 'Humidity (%)'])
                            csv_is_empty = False  # Update flag to indicate header is written
                        csv_writer.writerow([time_now.strftime('%Y-%m-%d %H:%M:%S'), co2, temp, hum])

                    # Limit data points to show only the last 20 points for each trace
                    max_points = 20
                    co2_data_trimmed = co2_data[-max_points:]
                    temp_data_trimmed = temp_data[-max_points:]
                    hum_data_trimmed = hum_data[-max_points:]
                    time_data_trimmed = time_data[-max_points:]

                    # Update traces with new data
                    with fig.batch_update():
                        fig.data[0].x = time_data_trimmed
                        fig.data[0].y = co2_data_trimmed
                        fig.data[1].x = time_data_trimmed
                        fig.data[1].y = temp_data_trimmed
                        fig.data[2].x = time_data_trimmed
                        fig.data[2].y = hum_data_trimmed

                except ValueError as e:
                    print(f"Error parsing data: {e}, data: {data}")

        time.sleep(1)  # Adjust sleep time as needed

# Function to update the plot with current data
def update_plot():
    # Update traces with final data
    fig.data[0].x = time_data
    fig.data[0].y = co2_data
    fig.data[1].x = time_data
    fig.data[1].y = temp_data
    fig.data[2].x = time_data
    fig.data[2].y = hum_data

    # Show final plot
    fig.show()

# Check if CSV file is empty
csv_is_empty = not csv_exists or os.stat(csv_filename).st_size == 0

# Start thread to read serial data
threading.Thread(target=read_serial_data, daemon=True).start()


# Keep the main thread alive until CTRL+C is pressed
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
