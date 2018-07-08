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


class WeatherApp(QtWidgets.QMainWindow):

    def __init__(self, fetcheddata: list, cidade: str, unidade: str):
        """
        Initializes a new WeatherApp object and creates the display window
        :param fetcheddata:
        :param cidade:
        :param unidade:
        """
        super(WeatherApp, self).__init__()
        self.setGeometry(50,50,300,400)
        self.setWindowTitle("Weather - Home")
        self.move(300, 100)

        self.lblBK = QtWidgets.QLabel(self)
        self.lblBK.setPixmap(QtGui.QPixmap("bk1.jpg"))
        self.lblBK.resize(300,400)
        self.lblBK.move(0,0)

        self.lblLogo = QtWidgets.QLabel(self)
        self.lblLogo.setPixmap(QtGui.QPixmap("logo.png"))
        self.lblLogo.setGeometry(30,5,200,40)

        icon_sunny = QPixmap("sunny1.png")
        icon_rainy = QPixmap("rainy.png")
        icon_snow = QPixmap("snow.png")
        icon_thunder = QPixmap("thunder.png")
        icon_cloudy = QPixmap("cloud.png")
        icons = [icon_sunny, icon_rainy, icon_snow, icon_thunder, icon_cloudy]

        font = QtGui.QFont()
        font.setItalic(True)
        font.setBold(True)
        font.setPointSize(55)

        font2 = QtGui.QFont()
        font2.setItalic(True)
        font2.setBold(True)
        font2.setPointSize(20)

        font3 = QtGui.QFont()
        font3.setItalic(True)
        font3.setBold(True)
        font3.setPointSize(14)

        actual_reading = round(fetcheddata[2],1)
        self.tempReading = QtWidgets.QLabel(str(actual_reading), self)
        self.tempReading.setGeometry(10,80,120,50)
        self.tempReading.setFont(font)

        self.displayUnits = QtWidgets.QLabel("ºF", self)
        if unidade.strip() == "metric":
            self.displayUnits.setText("ºC")
        self.displayUnits.setGeometry(140,80,30,30)
        self.displayUnits.setFont(font2)

        city = fetcheddata[0]
        self.city = QtWidgets.QLabel(str(city), self)
        self.city.setGeometry(10,130,120,30)
        self.city.setFont(font3)

        icon_weather = fetcheddata[1]
        self.icon = QtWidgets.QLabel(self)
        self.icon.setGeometry(170,20,180,180)
        if icon_weather == "clear sky":
            self.icon.setPixmap(icons[0])
        elif "haze" in icon_weather:
            self.icon.setPixmap(icons[4])
        elif "rain" in icon_weather:
            self.icon.setPixmap(icons[1])
        elif "cloud" in icon_weather:
            self.icon.setPixmap(icons[4])
        elif "snow" in icon_weather:
            self.icon.setPixmap(icons[2])
        elif "thunder" in icon_weather:
            self.icon.setPixmap(icons[3])

        self.lblReadings = QtWidgets.QLabel("Readings: ", self)
        self.lblReadings.setGeometry(20,200,100,30)
        self.lblReadings.setFont(font2)

        self.lblConditions = QtWidgets.QLabel("Conditions: " + icon_weather.upper(), self)
        self.lblConditions.setGeometry(20,230,220,30)

        self.lblTemp = QtWidgets.QLabel("Temperature: "+ str(actual_reading), self)
        self.lblTemp.setGeometry(20,260,120,30)

        self.lblMinTemp = QtWidgets.QLabel("Minimum: " + str(fetcheddata[4]), self)
        self.lblMinTemp.setGeometry(20,290,120,30)

        self.lblMaxTemp = QtWidgets.QLabel("Maximum: " + str(fetcheddata[3]), self)
        self.lblMaxTemp.setGeometry(20,320,120,30)

        self.lblHumidity = QtWidgets.QLabel("Humidity: " + str(fetcheddata[5]), self)
        self.lblHumidity.setGeometry(170,260,120,30)

        self.lblWindSpeed = QtWidgets.QLabel("Wind Speed: " + str(fetcheddata[6]), self)
        self.lblWindSpeed.setGeometry(170,290,120,30)


        self.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = WeatherApp()

    sys.exit(app.exec_())