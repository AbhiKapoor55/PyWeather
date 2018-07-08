"""Weather object that controls the application through its various propoerties."""

class WeatherObject:
    """A class of objects for displaying weather data"""
    def __init__(self, city: str) -> None:
        """Initializes an object of type WeatherObject.
        === Attributes ===
        city: string - the city for which the weather has to be obtained.
        temperature: integer - the temperature of the place searched.
        condition: integer - the weather condition at the place mentioned.
        """
        self.city = city
        self.temperature = 0
        self.condition = 0
        self.maxtemp = 0
        self.mintemp = 0
        self.humidity = 0
        self.windspeed = 0
        self.gust = 0
        self.direction = 0  # this is displayed as a bearing, with 0 being North direction.
        self.rain = 0
        self.clouds = 0