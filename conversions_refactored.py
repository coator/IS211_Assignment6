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

    class NoneTypeException(ValueError):
        pass

    class ConversionNotPossibleException(ValueError):
        pass

    class ConversionUnitInvalidError(ValueError):
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
        (1.00, -457.87),
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
        (10.0, 16093.44)
    )
    me_to_y_known_values = (
        (1.0, 1.09),
        (2.0, 2.19),
        (3.0, 3.28),
        (5.0, 5.47),
        (10.0, 10.94)
    )

    def test_me_to_y_table(self):
        """Tests all output numbers match result"""
        for meters, yards in self.me_to_y_known_values:
            result = convertMetersToYards(meters)
            self.assertEqual(yards, result)
        for meters, yards in self.me_to_y_known_values:
            result = convertYardsToMeters(yards)
            self.assertEqual(meters, result)

    def test_mi_to_y_table(self):
        """Tests all output numbers match result"""
        for a, b in self.mi_to_y_known_values:
            result = convertMilesToYards(a)
            self.assertEqual(b, result)
        for a, b in self.mi_to_y_known_values:
            result = convertYardsToMiles(b)
            self.assertEqual(a, result)

    def test_mi_to_me_table(self):
        """Tests all output numbers match result"""
        for a, b in self.mi_to_me_known_values:
            result = convertMilesToMeters(a)
            self.assertEqual(b, result)
        for a, b in self.mi_to_me_known_values:
            result = convertMetersToMiles(b)
            self.assertEqual(a, result)


    def test_kelvin_celsius_table(self):
        """Tests all output numbers match result"""
        for kelvin, celsius in self.k_to_c_known_values:
            result = convertKelvinToCelsius(kelvin)
            self.assertEqual(celsius, result)
        for kelvin, celsius in self.k_to_c_known_values:
            result = convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, result)

    def test_kelvin_fahrenheit_table(self):
        """Tests all output numbers match result"""
        for kelvin, fahrenheit in self.k_to_f_known_values:
            result = convertKelvinToFahrenheit(kelvin)
            self.assertEqual(fahrenheit, result)
        for kelvin, fahrenheit in self.k_to_f_known_values:
            result = convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(kelvin, result)

    def test_fahrenheit_celsius_table(self):
        """Tests all output numbers match result"""
        for fahrenheit, celsius in self.f_to_c_known_values:
            result = convertFahrenheitToCelsius(fahrenheit)
            self.assertEqual(celsius, result)
        for fahrenheit, celsius in self.f_to_c_known_values:
            result = convertCelsiusToFahrenheit(celsius)
            self.assertEqual(fahrenheit, result)


class InvalidIO(unittest.TestCase):

    def test_valid_measurement_category(self):
        """raises an ConversionUnitInvalidError if toUnit or fromUnit are not a valid unit type"""
        self.assertRaises(CustomExceptions.ConversionUnitInvalidError, convert, 'yards', 'cats', 2.0)

    def test_valid_measurement_types(self):
        """raises an ConversionNotPossibleException if inappropriate inputs are put together"""
        self.assertRaises(CustomExceptions.ConversionNotPossibleException, convert, 'meters', 'celsius', 2.0)

    def test_kelvin_input_negative(self):
        """raises an error if convertKelvinToCelsius, convertKelvinToFahrenheit input is negative"""
        test_function = convertKelvinToCelsius, convertKelvinToFahrenheit
        for i in test_function:
            self.assertRaises(CustomExceptions.OutOfRangeException, i, -5.0)

    def test_kelvin_output_negative(self):
        """raises an error if convertKelvinToCelsius, convertKelvinToFahrenheit is negative"""
        test_function = convertCelsiusToKelvin, convertFahrenheitToKelvin
        for i in test_function:
            self.assertRaises(CustomExceptions.OutOfRangeException, i, -1000000.0)

    def test_None_input(self):
        """raises an InvalidTypeException if input is None"""
        self.assertRaises(CustomExceptions.NoneTypeException, convert, 'yards', 'miles', None)

    def test_invalid_input(self):
        """raises TypeError exception if invalid type is put in"""
        self.assertRaises(CustomExceptions.InvalidTypeException, convert, 'yards', 'miles', 'a very wrong value')


def errorCheck(fromUnit, toUnit, value, units):
    def conversion_types(a, b):
        if a in units and b in units:
            pass
        else:
            if a not in units:
                raise CustomExceptions.ConversionUnitInvalidError('{} is not part of valid conversions'.format(a))
            else:
                raise CustomExceptions.ConversionUnitInvalidError('{} is not part of valid conversions'.format(b))

    conversion_types(fromUnit, toUnit)
    if not all(x in units[0:3] for x in [fromUnit, toUnit]):
        if not all(x in units[3:6] for x in [fromUnit, toUnit]):
            raise CustomExceptions.ConversionNotPossibleException(
                'Invalid Conversion types, cannot convert {} to {}'.format(fromUnit, toUnit))
    if value is None:
        raise CustomExceptions.NoneTypeException('Cannot be None')
    if not isinstance(value, float):
        raise CustomExceptions.InvalidTypeException('Must be a float')


def convert(fromUnit=str(), toUnit=str(), value=float()):
    units = ('miles', 'yards', 'meters', 'kelvin', 'celsius', 'fahrenheit')
    converttypes = convertCelsiusToKelvin, convertKelvinToCelsius, convertFahrenheitToKelvin, convertKelvinToFahrenheit, \
                   convertFahrenheitToCelsius, convertCelsiusToFahrenheit, convertMetersToMiles, convertMilesToMeters, \
                   convertYardsToMeters, convertMetersToYards, convertYardsToMiles, convertMilesToYards
    errorCheck(fromUnit, toUnit, value, units)
    value = float(value)
    convert_namespace = ('convert' + toUnit.capitalize() + 'To' + fromUnit.capitalize())
    for fn in converttypes:
        if convert_namespace == fn.__name__:
            print('converting {} to {}, results is {: f}'.format(fromUnit, toUnit, fn(value)))


def convertCelsiusToFahrenheit(n):
    """Convert Celsius to Fahrenheit"""
    return round(n * Fraction(9, 5) + 32, 2)


def convertFahrenheitToCelsius(n):
    """Convert Fahrenheit to Celsius"""
    return round((n - 32) * Fraction(5, 9), 2)


def convertFahrenheitToKelvin(n):
    """convert Fahrenheit to Kelvin"""
    nn = round((n +459.67)* Fraction(5,9), 2)
    if nn <= -1:
        raise CustomExceptions.OutOfRangeException('Kelvin cannot be negative, {} is showing negative'.format(nn))
    else:
        return nn

def convertKelvinToFahrenheit(n):
    """convert Kelvin to Fahrenheit"""

    if n <= -1:
        raise CustomExceptions.OutOfRangeException('Kelvin cannot be negative')

    return round(n * Fraction(9, 5) - float(459.67), 2)


def convertCelsiusToKelvin(n):
    """convert Celsius to Kelvin"""
    n = round(n + float(273.15), 2)
    if n <= -1:
        raise CustomExceptions.OutOfRangeException('Kelvin cannot be negative')
    else:
        return n


def convertKelvinToCelsius(n):
    """convert Kelvin to Celsius"""
    if n <= -1:
        raise CustomExceptions.OutOfRangeException('Kelvin cannot be negative')
    else:
        return round(n - float(273.15), 2)


def convertMilesToMeters(n):
    return round(n * 1609.344, 2)


def convertMetersToMiles(n):
    return round(n / 1609.344, 2)


def convertYardsToMeters(n):
    return round(n * 0.9144, 2)


def convertMetersToYards(n):
    return round(n * 1.09361, 2)


def convertYardsToMiles(n):
    return round(n * .000568182, 2)


def convertMilesToYards(n):
    return round(n * 1760, 2)


def main():
    inputd = input('Type u for unittest or press enter to run... ')
    if inputd == 'u':

        if __name__ == '__main__':
            unittest.main()

    else:
        while True:
            inputa, inputb, inputc = '', '', 0.0
            while len(inputa) == 0:
                inputa = input("Please type unit converting from: ")
                if inputa not in ('miles', 'yards', 'meters', 'kelvin', 'celsius', 'fahrenheit'):
                    inputa = ''
            while len(inputb) == 0:
                inputb = input("Please type unit converting input too: ")
                if inputa not in ('miles', 'yards', 'meters', 'kelvin', 'celsius', 'fahrenheit'):
                    inputb = ''
            while inputc == 0.0:
                inputc = float(input("Please type in amount: "))
            convert(inputa, inputb, inputc)
            print('___________________________________________________')


main()
