from temperature_converter import celsius_to_fahrenheit
from temperature_converter import fahrenheit_to_celsius

def test_celsius():
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit():
    assert fahrenheit_to_celsius(212) == 100