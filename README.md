
# Monitoring Application

This is a simple system monitoring application developed with Python and Kivy. It displays real-time network, CPU, memory, and disk I/O statistics.

## Prerequisites

Ensure you have the following installed on your PC:

- Python 3.7 or newer
- [Conda](https://docs.conda.io/en/latest/miniconda.html)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

1. **Clone the repository**

    Open your command line interface, navigate to your desired directory and run the following command:

    ```bash
    git clone https://github.com/username/MonitoringApp.git
    ```

    Don't forget to replace `username` with your GitHub username.

2. **Create and activate a new Conda environment**

    Navigate into the cloned project directory and create a new Conda environment:

    ```bash
    conda create --name myenv python=3.7
    conda activate myenv
    ```

3. **Install the project dependencies**

    Use pip to install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**

    Now you can run the application:

    ```bash
    python main.py
    or 
    navigate to root folder and run: python -m myapp.main
    ```

## Features

The application displays the following real-time system statistics:

- Network uptime
- Network latency
- Packet loss (network upload and download rates)
- CPU usage
- Memory
