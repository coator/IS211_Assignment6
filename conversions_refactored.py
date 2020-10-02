import unittest
from fractions import Fraction

"""
1. Check that all temperature conversions are working
2. Check that all distance conversions are working
3. Check that converting from one unit to itself returns the same value for all units
4. Check that converting from incompatible units will raise a ConversionNotPossibleexception
5. Check that from unit is float
6. Check that units are not 0 or None
7. Check that inputs fromUnit and ToUnit are string
8. Check that output is valid
9. Check that K is valid
(which should be defined in the conversions_refactored.py file)
"""


class CustomExceptions:
    class OutOfRangeException(ValueError):
        pass

    class InvalidTypeException(ValueError):
        pass

    class ConversionNotPossibleException(ValueError):
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
    mi_to_y_known_values = (
        (1.0, 1760.00),
        (2.0, 3520.00),
        (3.0, 5280.00),
        (5.0, 8800.00),
        (10.0, 17600.00)
    )
    mi_to_me_known_values = (
        (1.0, 1609.34),
        (2.0, 3218.69),
        (3.0, 4828.03),
        (5.0, 8046.72),
        (10.0, 16093.4)
    )
    me_to_y_known_values = (
        (1.0, 1.09361),
        (2.0, 2.18723),
        (3.0, 3.28084),
        (5.0, 5.46807),
        (10.0, 10.9361)
    )

    def test_kelvin_input_negative(self):
        """raises an error if Kelvin input is negative"""
        test_function = convertKelvinToCelsius, convertKelvinToFahrenheit
        for i in test_function:
            self.assertRaises(CustomExceptions.OutOfRangeException, i, -5.0)

    def test_kelvin_output_negative(self):
        """raises an error if Kelvin output is negative"""
        test_function = convertCelsiusToKelvin, convertFahrenheitToKelvin
        for i in test_function:
            self.assertRaises(CustomExceptions.OutOfRangeException, i, -1000000.0)

    def test_None_input(self):
        """raises an error if input is not a float"""
        test_function = convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToKelvin, \
                        convertFahrenheitToCelsius, convertKelvinToCelsius, convertKelvinToFahrenheit
        for i in test_function:
            self.assertRaises(CustomExceptions.InvalidTypeException, i, None)

    def test_invalid_input(self):
        test_function = convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToKelvin, \
                        convertFahrenheitToCelsius, convertKelvinToCelsius, convertKelvinToFahrenheit
        for i in test_function:
            self.assertRaises(CustomExceptions.InvalidTypeException, i, 'g')

    length_units = ('Miles', 'Yards', 'Meters')
    temperature_units = ('Kelvin', 'Celsius', 'Fahrenheit')


class ConvertTemps:
    def errorCheck(n):
        if not isinstance(n, float):
            raise CustomExceptions.InvalidTypeException('{} is a {}, it must be a float'.format(n, type(n)))
        if n is None:
            raise CustomExceptions.InvalidTypeException('Cannot be None')


if __name__ == '__main__':
    unittest.main()


def convert(fromUnit=str, toUnit=str, value=float):
    length_units = ('Miles', 'Yards', 'Meters')
    temperature_units = ('Kelvin', 'Celsius', 'Fahrenheit')


def convertCelsiusToFahrenheit(n):
    """convert Celsius to Fahrenheit"""
    ConvertTemps.errorCheck(n)
    return round(n * Fraction(5, 9) + 32, 2)


def convertFahrenheitToCelsius(n):
    """Convert Fahrenheit to Celsius"""
    ConvertTemps.errorCheck(n)
    return round((n - 32) * Fraction(5, 9), 2)


def convertFahrenheitToKelvin(n):
    """convert Fahrenheit to Kelvin"""
    ConvertTemps.errorCheck(n)
    round(n + float(459.67) * Fraction(9, 5), 2)
    if n <= -1:
        raise CustomExceptions.OutOfRangeException('Kelvin cannot be negative')
    else:
        return n


def convertKelvinToFahrenheit(n):
    """convert Kelvin to Fahrenheit"""
    ConvertTemps.errorCheck(n)

    if n <= -1:
        raise CustomExceptions.OutOfRangeException('Kelvin cannot be negative')

    return round(n * Fraction(9, 5) - float(459.67), 2)


def convertCelsiusToKelvin(n):
    """convert Celsius to Kelvin"""
    ConvertTemps.errorCheck(n)
    n = round(n + float(273.15), 2)
    if n <= -1:
        raise CustomExceptions.OutOfRangeException('Kelvin cannot be negative')
    else:
        return n


def convertKelvinToCelsius(n):
    """convert Kelvin to Celsius"""
    ConvertTemps.errorCheck(n)
    if n <= -1:
        raise CustomExceptions.OutOfRangeException('Kelvin cannot be negative')
    else:
        return round(n - float(273.15), 2)



if __name__ == '__main__':
    unittest.main()
