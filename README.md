# CO2 Forecasting

This repository contains scripts and notebooks for forecasting CO2 levels using data from an STM32 CO2 sensor. The project involves collecting sensor data, enhancing it, and using time series forecasting models to predict future CO2 levels.

## Overview

The repository is divided into several parts:

1. **Data Collection**: A Python script for reading UART data from the STM32 CO2 sensor, saving it to a CSV file, and plotting the collected data when stopped with **CTRL+C**.
2. **Data Enhancement**: A Python script for preprocessing the data by adding lags, splitting dates, and handling occupancy.
3. **Forecasting**: A Colab notebook that performs time series forecasting on the enhanced data using SARIMAX models.

## Table of Contents

- [Introduction](#introduction)
- [STM32 Projects](#stm32-projects)
- [Data Collection](#data-collection)
- [Data Processing](#data-processing)
- [Time Series Analysis](#time-series-analysis)
- [Results](#results)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project aims to forecast CO2 levels using data collected from an STM32-based CO2 sensor. The data is processed and analyzed using Python libraries to create predictive models.

## STM32 Projects

This project leverages the following STM32 projects:
- [STM32 SDC30 CO2 Sensor](https://github.com/cherifon/STM32_SDC30_CO2_Sensor): Project for interfacing with the SDC30 CO2 sensor.
- [STM32 16x2 LCD](https://github.com/cherifon/STM32_16x2_LCD): Project for displaying data on a 16x2 LCD screen.

## Data Collection

The data is collected using the STM32 SDC30 CO2 sensor project. The sensor measures CO2 levels and logs the data, which is then transferred for processing and analysis.

## Data Processing

Data processing involves cleaning and preparing the dataset for analysis. The steps include:
- Handling missing values
- Removing infinite values
- Normalizing the data
- Creating lag features

## Time Series Analysis

Time series analysis is performed using the SARIMAX model to forecast future CO2 levels. The analysis includes:
- Checking for stationarity
- Differencing the data if necessary
- Auto ARIMA to find the best model parameters
- Fitting the SARIMAX model

## Results

The results include the forecasted CO2 levels compared to the actual data. The predictions are visualized to show the accuracy of the model.

## Usage

To use this project:
1. Clone the repository.
2. Install the necessary Python libraries.
3. Run the data processing and analysis scripts.
4. Use the provided Jupyter notebooks for detailed analysis and visualization.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, contact [cherifjebali0301@gmail.com](mailto:cherifjebali0301@gmail.com).
