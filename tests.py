import unittest
import conversions

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

    def test_kelvin_celsius_table(self):
        """if true will give known result with known input, if false will give known give in backwards order"""
        for kelvin, celsius in self.k_to_c_known_values:
            result = conversions.convertKelvinToCelsius(kelvin)
            self.assertEqual(celsius, result)
        for kelvin, celsius in self.k_to_c_known_values:
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, result)

    def test_kelvin_fahrenheit_table(self):
        """if true will give known result with known input, if false will give known give in backwards order"""
        for kelvin, fahrenheit in self.k_to_f_known_values:
            result = conversions.convertKelvinToFahrenheit(kelvin)
            self.assertEqual(fahrenheit, result)
        for kelvin, fahrenheit in self.k_to_f_known_values:
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(kelvin, result)

    def test_fahrenheit_celsius_table(self):
        """if true will give known result with known input, if false will give known give in backwards order"""
        for fahrenheit, celsius in self.f_to_c_known_values:
            result = conversions.convertFahrenheitToCelsius(fahrenheit)
            self.assertEqual(celsius, result)
        for fahrenheit, celsius in self.f_to_c_known_values:
            result = conversions.convertCelsiusToFahrenheit(celsius)
            self.assertEqual(fahrenheit, result)


class ConvertKelvinNegative(unittest.TestCase):
    def test_kelvin_input_negative(self):
        """raises an error if Kelvin input is negative"""
        test_function = conversions.convertKelvinToCelsius, conversions.convertKelvinToFahrenheit
        for i in test_function:
            self.assertRaises(conversions.ModuleErrors.OutOfRangeException, i, -5.0)

    def test_kelvin_output_negative(self):
        """raises an error if Kelvin output is negative"""
        test_function = conversions.convertCelsiusToKelvin, conversions.convertFahrenheitToKelvin
        for i in test_function:
            self.assertRaises(conversions.ModuleErrors.OutOfRangeException, i, -1000000.0)


class InvalidTypeInput(unittest.TestCase):
    def test_None_input(self):
        """raises an error if input is blank"""
        test_function = conversions.convertCelsiusToKelvin, conversions.convertCelsiusToFahrenheit, conversions.convertFahrenheitToKelvin, \
                        conversions.convertFahrenheitToCelsius, conversions.convertKelvinToCelsius, conversions.convertKelvinToFahrenheit
        for i in test_function:
            self.assertRaises(conversions.ModuleErrors.InvalidTypeException, i, None)

    def test_invalid_input(self):
        """raises an error if input is not a float"""
        test_function = conversions.convertCelsiusToKelvin, conversions.convertCelsiusToFahrenheit, conversions.convertFahrenheitToKelvin, \
                        conversions.convertFahrenheitToCelsius, conversions.convertKelvinToCelsius, conversions.convertKelvinToFahrenheit
        for i in test_function:
            self.assertRaises(conversions.ModuleErrors.InvalidTypeException, i, 'g')


if __name__ == '__main__':
    unittest.main()