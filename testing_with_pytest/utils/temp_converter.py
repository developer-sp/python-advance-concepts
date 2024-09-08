class UnsupportedTemperature(Exception):
    pass


def temperature_converter(value: float, from_unit: str, to_unit: str) -> float:
    conversions = {
        "Celsius": {
            "Fahrenheit": lambda c: (c * 9/5) + 32,
            "Kelvin": lambda c: c + 273.15,
        },
        "Fahrenheit": {
            "Celsius": lambda f: (f - 32) * 5/9,
            "Kelvin": lambda f: (f - 32) * 5/9 + 273.15,
        },
        "Kelvin": {
            "Celsius": lambda k: k - 273.15,
            "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32,
        }
    }

    if from_unit == to_unit:
        return value

    if from_unit not in conversions.keys():
        raise UnsupportedTemperature(f"Unit {from_unit} is not supported")

    if to_unit not in conversions.keys():
        raise UnsupportedTemperature(f"Unit {to_unit} is not supported")

    return conversions[from_unit][to_unit](value)