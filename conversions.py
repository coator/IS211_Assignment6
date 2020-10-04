import unittest
from fractions import Fraction

"""

rules:
1. there is no negative K (Kelvin approaches 0, and does not go beyond that)
2. it MUST be a float input
3. Cannot be None


"""


class ModuleErrors:
    class OutOfRangeException(ValueError):
        pass

    class InvalidTypeException(ValueError):
        pass



def errorCheck(n):
    if not isinstance(n, float):
        raise ModuleErrors.InvalidTypeException('{} is a {}, it must be a float'.format(n, type(n)))
    if n is None:
        raise ModuleErrors.InvalidTypeException('Cannot be None')


def convertKelvinToCelsius(n):
    """convert Kelvin to Celsius"""
    errorCheck(n)
    if n <= -1:
        raise ModuleErrors.OutOfRangeException('Kelvin cannot be negative')
    else:
        return round(n - float(273.15), 2)


def convertCelsiusToKelvin(n):
    """convert Celsius to Kelvin"""
    errorCheck(n)
    n = round(n + float(273.15), 2)
    if n <= -1:
        raise ModuleErrors.OutOfRangeException('Kelvin cannot be negative')
    else:
        return n


def convertKelvinToFahrenheit(n):
    """convert Kelvin to Fahrenheit"""
    errorCheck(n)
    if n <= -1:
        raise ModuleErrors.OutOfRangeException('Kelvin cannot be negative')

    return round(n * Fraction(9, 5) - float(459.67), 2)


def convertFahrenheitToKelvin(n):
    """convert Fahrenheit to Kelvin"""
    errorCheck(n)
    nn = round((n + 459.67) * Fraction(5, 9), 2)
    if nn <= -1:
        raise ModuleErrors.OutOfRangeException('Kelvin cannot be negative, {} is showing negative'.format(nn))
    else:
        return nn


def convertFahrenheitToCelsius(n):
    """Convert Fahrenheit to Celsius"""
    errorCheck(n)
    return round((n - 32) * Fraction(5, 9), 2)


def convertCelsiusToFahrenheit(n):
    """convert Celsius to Fahrenheit"""
    errorCheck(n)
    return round(n * Fraction(9, 5) + 32, 2)
