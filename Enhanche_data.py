import pandas as pd

# Load data
data = pd.read_csv('sensor_data.csv')

# Convert Timestamp to datetime
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Extract time-based features
data['Hour'] = data['Timestamp'].dt.hour
data['Day'] = data['Timestamp'].dt.day
data['Month'] = data['Timestamp'].dt.month
data['DayOfWeek'] = data['Timestamp'].dt.dayofweek

# Lag features (previous values)
data['CO2_lag1'] = data['CO2 (ppm)'].shift(1)
data['Temp_lag1'] = data['Temperature (�C)'].shift(1)
data['Hum_lag1'] = data['Humidity (%)'].shift(1)

# Drop NA values created by lag features
data = data.dropna()

# Save the enhanced dataset
data.to_csv('enhanced_sensor_data.csv', index=False)

# Load your dataset
data = pd.read_csv('enhanced_sensor_data.csv')

data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Manually label the data
data['Occupancy'] = 1  # Assume the room is occupied by default
data.loc[(data['Hour'] == 9), 'Occupancy'] = 1
data.loc[(data['Hour'] == 12), 'Occupancy'] = 0
data.loc[(data['Day'] == 19) & (data['Hour'] == 12), 'Occupancy'] = 1  
# Save the labeled dataset
data.to_csv('labeled_sensor_data.csv', index=False)
