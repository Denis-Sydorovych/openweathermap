import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ResponsJsonWeatherByCoordinates(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_correct_response_json_weather_by_zip(self):
        driver = self.driver
        driver.get("http://api.openweathermap.org/data/2.5/weather?lat=50.09&lon=31.48")
        assert '"name":"Pereyaslav-Khmelnytskyy"' in driver.page_source
        assert '"country":"UA"' in driver.page_source
        assert '"coord":{"lon":31.48,"lat":50.09},"' in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
