import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt6.QtGui import QPixmap, QPalette, QColor
import requests

def get_weather_data(api_key, city, country_code):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Error al obtener los datos del clima")
        return None

def get_city_coordinates(city):
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data:
            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
            return lat, lon
    print("Error al obtener las coordenadas de la ciudad")
    return None

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')

        self.country_label = QLabel('Country Code:')
        self.country_input = QLineEdit()

        self.city_label = QLabel('City:')
        self.city_input = QLineEdit()

        self.submit_button = QPushButton('Get Weather')
        self.submit_button.clicked.connect(self.get_weather)

        self.latitude_label = QLabel('Latitude:')
        self.longitude_label = QLabel('Longitude:')
        self.latitude_value = QLabel()
        self.longitude_value = QLabel()

        self.temperature_icon = QLabel()
        temperature_icon_pixmap = QPixmap("noun-temperature-5874440.png")  # Ruta al archivo de imagen del icono de temperatura
        temperature_icon_pixmap = temperature_icon_pixmap.scaled(50, 50)  # Reducir el tamaño del ícono a 50x50 píxeles
        self.temperature_icon.setPixmap(temperature_icon_pixmap)

        self.humidity_icon = QLabel()
        humidity_icon_pixmap = QPixmap("noun-humidity-1957572.png")  # Ruta al archivo de imagen del icono de humedad
        humidity_icon_pixmap = humidity_icon_pixmap.scaled(50, 50)  # Reducir el tamaño del ícono a 50x50 píxeles
        self.humidity_icon.setPixmap(humidity_icon_pixmap)

        self.temperature_label = QLabel('Temperature:')
        self.humidity_label = QLabel('Humidity:')
        self.temperature_value = QLabel()
        self.humidity_value = QLabel()

        self.weather_label = QLabel()

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#FFFFFF"))  # Color de fondo blanco
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#000000"))  # Color de texto negro
        self.setPalette(palette)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.city_label)
        input_layout.addWidget(self.city_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_button)

        coordinates_layout = QGridLayout()
        coordinates_layout.addWidget(self.latitude_label, 0, 0)
        coordinates_layout.addWidget(self.latitude_value, 0, 1)
        coordinates_layout.addWidget(self.longitude_label, 1, 0)
        coordinates_layout.addWidget(self.longitude_value, 1, 1)

        icon_layout = QVBoxLayout()
        icon_layout.addWidget(self.temperature_icon)
        icon_layout.addWidget(self.humidity_icon)

        data_layout = QVBoxLayout()
        data_layout.addWidget(self.temperature_label)
        data_layout.addWidget(self.temperature_value)
        data_layout.addWidget(self.humidity_label)
        data_layout.addWidget(self.humidity_value)

        weather_layout = QHBoxLayout()
        weather_layout.addLayout(icon_layout)
        weather_layout.addLayout(data_layout)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.country_label, 0, 0)
        grid_layout.addWidget(self.country_input, 0, 1)
        grid_layout.addLayout(input_layout, 1, 0, 1, 2)
        grid_layout.addLayout(button_layout, 1, 2)
        grid_layout.addLayout(weather_layout, 2, 0, 1, 3)
        grid_layout.addLayout(coordinates_layout, 3, 0, 1, 2)
        grid_layout.addWidget(self.weather_label, 4, 0, 1, 3)

        main_layout = QVBoxLayout()
        main_layout.addLayout(grid_layout)

        self.setLayout(main_layout)

    def get_weather(self):
        api_key = "6c5275ac06a3825bf7684892bd381b27"  # Reemplaza con tu clave de API de OpenWeatherMap
        country_code = self.country_input.text()
        city = self.city_input.text()

        weather_data = get_weather_data(api_key, city, country_code)

        if weather_data:
            temperature_kelvin = weather_data['main']['temp']
            temperature_celsius = temperature_kelvin - 273.15  # Conversión de Kelvin a Celsius
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']

            result = f"Description: {description}"
            self.weather_label.setText(result)
            self.temperature_value.setText(f"{temperature_celsius:.2f} °C")
            self.humidity_value.setText(f"{humidity}%")
        else:
            self.weather_label.setText('Error al obtener los datos del clima')
            self.temperature_value.setText('N/A')
            self.humidity_value.setText('N/A')

        coordinates = get_city_coordinates(city)
        if coordinates:
            latitude, longitude = coordinates
            self.latitude_value.setText(f"{latitude:.2f}")
            self.longitude_value.setText(f"{longitude:.2f}")
        else:
            self.latitude_value.setText('N/A')
            self.longitude_value.setText('N/A')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec())
