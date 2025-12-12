"""Module for building car dictionaries."""

def build_car(constructor, model_name, **other):
    """Build a dictionary representing a car."""
    other["constructor"] = constructor
    other["model_name"] = model_name
    return other