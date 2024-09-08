import pytest
from utils.temp_converter import UnsupportedTemperature, temperature_converter

# # This whole thing is a single test
# def test_temperature_converter_convert_units():
#     # Celsius
#     assert temperature_converter(0, 'Celsius', 'Kelvin') == 273.15
#     assert temperature_converter(0, 'Celsius', 'Fahrenheit') == 32

#     # Kelvin
#     assert temperature_converter(273.15, 'Kelvin', 'Celsius') == 0
#     assert temperature_converter(273.15, 'Kelvin', 'Fahrenheit') == 32

#     # Celsius
#     assert temperature_converter(32, 'Fahrenheit', 'Kelvin') == 273.15
#     assert temperature_converter(32, 'Fahrenheit', 'Celsius') == 0

#     # Same From and To
#     assert temperature_converter(0, 'Fahrenheit', 'Fahrenheit') == 0
#     assert temperature_converter(0, 'Kelvin', 'Kelvin') == 0
#     assert temperature_converter(0, 'Celsius', 'Celsius') == 0

# def test_unspported_types():
#     with pytest.raises(UnsupportedTemperature):
#         temperature_converter(273.15, 'Kelvin', 'MyCelsius')

#     with pytest.raises(UnsupportedTemperature):
#         temperature_converter(273.15, 'MyKelvin', 'Celsius')

# # here, this is very similar to the first test, by writing it in an easy format
# @pytest.mark.parametrize("value, from_unit, to_unit, expected_value",[
#     (0, 'Celsius', 'Kelvin', 273.15),
#     (0, 'Celsius', 'Fahrenheit', 32),
#     (273.15, 'Kelvin', 'Celsius', 0),
#     (273.15, 'Kelvin', 'Fahrenheit', 32),
#     (32, 'Fahrenheit', 'Kelvin', 273.15),
#     (32, 'Fahrenheit', 'Celsius', 0),
#     (0, 'Fahrenheit', 'Fahrenheit', 0),
#     (0, 'Kelvin', 'Kelvin', 0),
#     (0, 'Celsius', 'Celsius', 0)
# ])
# def test_temperature_converter_convert_units_parameterize(value: int, from_unit: str, to_unit: str, expected_value: float):
#     assert temperature_converter(value, from_unit, to_unit) == expected_value


# As all of above tests are for a particular function, we can group them in a class

class TestTemperatureConverter:
    # This whole thing is a single test
    def test_temperature_converter_convert_units(self):
        # Celsius
        assert temperature_converter(0, 'Celsius', 'Kelvin') == 273.15
        assert temperature_converter(0, 'Celsius', 'Fahrenheit') == 32

        # Kelvin
        assert temperature_converter(273.15, 'Kelvin', 'Celsius') == 0
        assert temperature_converter(273.15, 'Kelvin', 'Fahrenheit') == 32

        # Celsius
        assert temperature_converter(32, 'Fahrenheit', 'Kelvin') == 273.15
        assert temperature_converter(32, 'Fahrenheit', 'Celsius') == 0

        # Same From and To
        assert temperature_converter(0, 'Fahrenheit', 'Fahrenheit') == 0
        assert temperature_converter(0, 'Kelvin', 'Kelvin') == 0
        assert temperature_converter(0, 'Celsius', 'Celsius') == 0

    def test_unspported_types(self):
        with pytest.raises(UnsupportedTemperature):
            temperature_converter(273.15, 'Kelvin', 'MyCelsius')

        with pytest.raises(UnsupportedTemperature):
            temperature_converter(273.15, 'MyKelvin', 'Celsius')

    # here, this is very similar to the first test, by writing it in an easy format
    # the pytest.mark.parametrize takes in a  string containing the parameters expected by the func
    # to be tested, the expected value and a list of tuples containig different parameters
    # each tuple is a test. Hence total there will be 9 tests for the below
    @pytest.mark.parametrize("value, from_unit, to_unit, expected_value",[
        (0, 'Celsius', 'Kelvin', 273.15),
        (0, 'Celsius', 'Fahrenheit', 32),
        (273.15, 'Kelvin', 'Celsius', 0),
        (273.15, 'Kelvin', 'Fahrenheit', 32),
        (32, 'Fahrenheit', 'Kelvin', 273.15),
        (32, 'Fahrenheit', 'Celsius', 0),
        (0, 'Fahrenheit', 'Fahrenheit', 0),
        (0, 'Kelvin', 'Kelvin', 0),
        (0, 'Celsius', 'Celsius', 0)
    ])
    def test_temperature_converter_convert_units_parameterize(self, value: int, from_unit: str, to_unit: str, expected_value: float):
        assert temperature_converter(value, from_unit, to_unit) == expected_value


# you can run a particular test by calling
# pytest tests/unit/utils/test_temp_converter.py::TestTemperatureConverter

# You can also run an individual test func inside the class
# pytest tests/unit/utils/test_temp_converter.py::TestTemperatureConverter::test_temperature_converter_convert_units_parameterize