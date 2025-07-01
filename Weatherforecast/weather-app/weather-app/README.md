# FILE: /weather-app/weather-app/README.md

# Weather Application

This is a simple weather application built in Python that provides current weather information for a specified city. The application features a graphical user interface (GUI) that displays temperature, wind speed, date, and time.

## Features

- Fetches weather data from a weather API.
- Displays temperature, wind speed, date, and time.
- User-friendly graphical interface.

## Requirements

- Python 3.x
- Tkinter or PyQt (for GUI)
- Requests (for API calls)
- python-dotenv (for environment variable management)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd weather-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the root directory and add your weather API key:
     ```
     WEATHER_API_KEY=your_api_key_here
     ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Enter the name of the city you want to check the weather for.

3. The application will display the current weather information.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.