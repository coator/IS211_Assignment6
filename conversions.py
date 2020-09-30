import unittest

"""

rules:
1. there is no negative K (Kelvin approaches 0, and does not go beyond that)
2. it MUST be a float input


"""


def convertKelvinToCelsius(n=float()):
    return n


def convertCelsiusToKelvin(n=float()):
    return n


def convertKelvinToFahrenheit(n=float()):
    return n


def convertFahrenheitToKelvin(n=float()):
    return n


def convertFahrenheitToCelsius(n=float()):
    return n


def convertCelsiusToFahrenheit(n=float()):
    return n


class KnownValues(unittest.TestCase):
    k_to_c_known_values = (
        (0.00, -273.15),
        (15.00, -258.15),
        (30.05, -243.1),
        (300, 26.85),
        (450, 176.85),
    )

    k_to_f_known_values = (
        (0, -459.67),
        (15, -432.67),
        (30.05, -405.58),
        (300, 80.33),
        (450, 350.22),
    )

    f_to_c_known_values = (
        (-459.67, -273.15),
        (-432.67, 258.15),
        (-405.58, -243.1),
        (80.33, 26.85),
        (350.22, 176.85),
        (50.00, 10.00),
        (72.00, 22.22)
    )


    def test_kelvin_celsius_table(self, forwards=True):
        """if true will give known result with known input, if false will give known give in backwards order"""
        if forwards:
            for kelvin, celsius in self.k_to_f_known_values:
                result = convertKelvinToCelsius(kelvin)
                self.assertEqual(celsius, result)
        else:
            for kelvin, celsius in self.k_to_f_known_values:
                result = convertCelsiusToKelvin(celsius)
                self.assertEqual(kelvin, result)

    def test_kelvin_fahrenheit_table(self, forwards=True):
        """if true will give known result with known input, if false will give known give in backwards order"""
        if forwards:
            for kelvin, fahrenheit in self.k_to_f_known_values:
                result = convertKelvinToFahrenheit(kelvin)
                self.assertEqual(fahrenheit, result)
        else:
            for kelvin, fahrenheit in self.k_to_f_known_values:
                result = convertFahrenheitToKelvin(fahrenheit)
                self.assertEqual(kelvin, result)

    def test_fahrenheit_celsius_table(self, forwards=True):
        """if true will give known result with known input, if false will give known give in backwards order"""
        if forwards:
            for fahrenheit, celsius in self.k_to_f_known_values:
                result = convertFahrenheitToCelsius(fahrenheit)
                self.assertEqual(celsius, result)
        else:
            for fahrenheit, celsius in self.k_to_f_known_values:
                result = convertCelsiusToFahrenheit(celsius)
                self.assertEqual(fahrenheit, result)
