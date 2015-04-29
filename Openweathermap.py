import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ResponseJsonWeatherByZip(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_correct_response_json_weather_by_zip(self):
        driver = self.driver
        driver.get("http://api.openweathermap.org/data/2.5/weather?zip=22222,us")
        assert '"name":"Arlington"', '"country":"US"' in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()