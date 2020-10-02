import unittest
from fractions import Fraction

"""

rules:
1. there is no negative K (Kelvin approaches 0, and does not go beyond that)
2. it MUST be a float input
3. Cannot be None


"""


class ModuleErrors:
    class OutOfRangeError(ValueError):
        pass

    class InvalidTypeError(ValueError):
        pass


class KnownValues(unittest.TestCase):
    k_to_c_known_values = (
        (0.00, -273.15),
        (15.00, -258.15),
        (30.05, -243.1),
        (300.00, 26.85),
        (450.00, 176.85)
    )

    k_to_f_known_values = (
        (0.00, -459.67),
        (15.00, -432.67),
        (30.05, -405.58),
        (300.00, 80.33),
        (450.00, 350.33)
    )

    f_to_c_known_values = (
        (-459.67, -273.15),
        (-432.67, -258.15),
        (-405.58, -243.1),
        (80.33, 26.85),
        (350.33, 176.85),
        (50.00, 10.00),
        (72.00, 22.22)
    )

    def test_kelvin_celsius_table(self, forwards=True):
        """if true will give known result with known input, if false will give known give in backwards order"""
        if forwards:
            for kelvin, celsius in self.k_to_c_known_values:
                result = convertKelvinToCelsius(kelvin)
                self.assertEqual(celsius, result)
        else:
            for kelvin, celsius in self.k_to_c_known_values:
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
            for fahrenheit, celsius in self.f_to_c_known_values:
                result = convertFahrenheitToCelsius(fahrenheit)
                self.assertEqual(celsius, result)
        else:
            for fahrenheit, celsius in self.f_to_c_known_values:
                result = convertCelsiusToFahrenheit(celsius)
                self.assertEqual(fahrenheit, result)


class ConvertKelvinNegative(unittest.TestCase):
    def test_kelvin_input_negative(self):
        """raises an error if Kelvin input is negative"""
        test_function = convertKelvinToCelsius, convertKelvinToFahrenheit
        for i in test_function:
            self.assertRaises(ModuleErrors.OutOfRangeError, i, -5.0)

    def test_kelvin_output_negative(self):
        """raises an error if Kelvin output is negative"""
        test_function = convertCelsiusToKelvin, convertFahrenheitToKelvin
        for i in test_function:
            self.assertRaises(ModuleErrors.OutOfRangeError, i, -1000000.0)


class InvalidTypeInput(unittest.TestCase):
    def test_None_input(self):
        """raises an error if input is not a float"""
        test_function = convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToKelvin, \
                        convertFahrenheitToCelsius, convertKelvinToCelsius, convertKelvinToFahrenheit
        for i in test_function:
            self.assertRaises(ModuleErrors.InvalidTypeError, i, None)

    def test_invalid_input(self):
        test_function = convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToKelvin, \
                        convertFahrenheitToCelsius, convertKelvinToCelsius, convertKelvinToFahrenheit
        for i in test_function:
            self.assertRaises(ModuleErrors.InvalidTypeError, i, 'g')


# TODO: getting InvalidTypeError for valid types. need to investigate
def errorCheck(n):
    if not isinstance(n, float):
        raise ModuleErrors.InvalidTypeError('{} is a {}, it must be a float'.format(n, type(n)))
    if n is None:
        raise ModuleErrors.InvalidTypeError('Cannot be None')


def convertKelvinToCelsius(n):
    """convert Kelvin to Celsius"""
    errorCheck(n)
    if n <= -1:
        raise ModuleErrors.OutOfRangeError('Kelvin cannot be negative')
    else:
        return round(n - float(273.15), 2)


def convertCelsiusToKelvin(n):
    """convert Celsius to Kelvin"""
    errorCheck(n)
    n = round(n + float(273.15), 2)
    if n <= -1:
        raise ModuleErrors.OutOfRangeError('Kelvin cannot be negative')
    else:
        return n


def convertKelvinToFahrenheit(n):
    """convert Kelvin to Fahrenheit"""
    errorCheck(n)

    if n <= -1:
        raise ModuleErrors.OutOfRangeError('Kelvin cannot be negative')

    return round(n * Fraction(9, 5) - float(459.67), 2)


def convertFahrenheitToKelvin(n):
    """convert Fahrenheit to Kelvin"""
    errorCheck(n)
    round(n + float(459.67) * Fraction(9, 5), 2)
    if n <= -1:
        raise ModuleErrors.OutOfRangeError('Kelvin cannot be negative')
    else:
        return n


def convertFahrenheitToCelsius(n):
    """Convert Fahrenheit to Celsius"""
    errorCheck(n)
    return round((n - 32) * Fraction(5, 9), 2)


def convertCelsiusToFahrenheit(n):
    """convert Celsius to Fahrenheit"""
    errorCheck(n)
    return round(n * Fraction(5, 9) + 32, 2)


if __name__ == '__main__':
    unittest.main()
