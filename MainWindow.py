"""
===============================================================================
File: MainWindow.py
Author: Abhi Kapoor, Sultan Sidhu
Date: July 5th, 2018
Purpose: This file creates the initial main window screen for pyWeather
===============================================================================
"""

import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PIL import *

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from object import WeatherObject
import json
import urllib.request
import WeatherApp


API_KEY = "babdc724b27b2b5293d207a385e0d7d4"
URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}"
COURSE_IS_OVER = False


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        """
        Initializes a new MainWindow object, and creates the display screen
        """
        super(MainWindow, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("pyWeather - Enter City and Units")

        label2 = QtWidgets.QLabel(self)
        label2.move(0,0)
        label2.resize(350,250)

        self.status_txt = QtWidgets.QLabel(self)
        self.status_txt.move(0,0)
        movie = QtGui.QMovie("sunny.gif")
        self.status_txt.setMovie(movie)
        self.status_txt.resize(600,300)
        movie.start()

        font = QtGui.QFont()
        font.setItalic(True)
        font.setBold(True)
        font.setPointSize(10)

        self.lblCopyrightInfo = QtWidgets.QLabel("© Copyright Sultan Sidhu and Abhi Kapoor 2018", self)
        self.lblCopyrightInfo.setGeometry(250, 270, 300, 30)
        self.lblCopyrightInfo.setFont(font)

        self.lblName = QtWidgets.QLabel("Enter a city: ", self)
        self.lblName.setGeometry(115,125,100,30)
        self.lblName.setFont(font)

        self.lblUnits = QtWidgets.QLabel("Units: Metric or Imperial? ", self)
        self.lblUnits.setGeometry(255, 125, 200, 30)
        self.lblUnits.setFont(font)

        self.e1 = QtWidgets.QLineEdit(self)
        self.e1.resize(125,20)
        self.e1.move(115,150)

        self.e2 = QtWidgets.QLineEdit(self)
        self.e2.resize(125,20)
        self.e2.move(255,150)
        self.e2.returnPressed.connect(self.search_slot)

        self.show()

    def search_slot(self):
        self.lblName.setText("Loading...")
        self.lblName.repaint()
        self.lblUnits.setText(" ")
        self.lblUnits.repaint()
        cidade = self.e1.text().strip()
        unidade = self.e2.text().strip()
        print("cidade is ", cidade, " and unidade is ", unidade)

        completed = 0
        while completed < 100:
            completed += 0.00001
            # if round(completed) == 85:
            #     self.lblName.setText("Fetching Data...")
            #     self.lblName.repaint()

        self.lblName.setText("Fetching Data...")
        self.lblName.repaint()
        self.display_app()
        self.lblName.setText("Data Received")
        # --------- delete this later, its just to see how it looks -------------

        self.screen2 = WeatherApp.WeatherApp(self.fetcheddata, cidade, unidade)
        self.screen2.show()
        self.screen2.setWindowTitle("pyWeather - Home")

        # --------- delete this later, its just to see how it looks -------------

        self.e1.setText("")
        self.e2.setText("")

    def display_app(self) -> None:
        """The main function for the display of the app"""
        self.fetcheddata = self.run_app()
        print("------------------------------")
        print(self.fetcheddata)
        print("------------------------------")

        # COURSE_IS_OVER = False
        # response = input("Would you like to rerun the app? ")
        # rerun_app(response)

    def run_app(self) -> list:
        """"A function that runs the app!"""
        # URL = "api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}"
        CITY = self.e1.text().strip()
        # FINALURL = URL + CITY + "}"
        weatherJSON = self.html_request(CITY, API_KEY, self.unitselector())
        newweatherobject = WeatherObject(CITY)
        # print(weatherJSON)
        newdata = self.updateweatherdata(newweatherobject, weatherJSON)

        return newdata
        # TODO: COMPLETE THIS FUNCTION. THIS FUNCTION IS THE CENTRAL FUNCTION OF THE PROGRAM.

    def html_request(self,city, api_key, units) -> json:
        """Places HTML request for weather data, returns a JSON object with all the concurrent weather data."""
        weatherdata = urllib.request.urlopen(URL.format(city, api_key, units))

        # print(weatherdata)
        # weather = weatherdata.read()
        jsonweather = json.load(weatherdata)
        return jsonweather

    def unitselector(self) -> str:
        """selects the units based on individual preferences"""
        # query = input("How would you like your units? Imperial or metric? ")
        query = self.e2.text().strip()
        return query

    def updateweatherdata(self,weatherob: 'WeatherObject', inputjson: json) -> list:
        """Returns a list of all the required weather data fields sourced from the input weather json."""
        weatherob.city = inputjson['name']
        weatherob.condition = inputjson['weather'][0]['description']
        weatherob.temperature = inputjson['main']['temp']
        weatherob.maxtemp = inputjson['main']['temp_max']
        weatherob.mintemp = inputjson['main']['temp_min']
        weatherob.humidity = inputjson['main']['humidity']
        weatherob.windspeed = inputjson['wind']['speed']
        # weatherob.gust = inputjson['wind']['gust']
        weatherob.direction = inputjson['wind']['deg']
        # weatherob.rain = inputjson['rain']['1h']
        weatherob.clouds = inputjson['clouds']['all']

        return [weatherob.city, weatherob.condition, weatherob.temperature, weatherob.maxtemp, weatherob.mintemp,
                weatherob.humidity, weatherob.windspeed, weatherob.direction, weatherob.clouds]


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = MainWindow()

    sys.exit(app.exec_())