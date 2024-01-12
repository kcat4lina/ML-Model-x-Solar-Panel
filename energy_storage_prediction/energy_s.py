import math

def calculate_energy_stored(light_intensity, k, n):
    """Calculates the energy stored in a photoresistor based on light intensity.

    Args:
        light_intensity (float): The light intensity (in lux).
        k (float): A constant that depends on the photoresistor's size and sensitivity.
        n (float): A coefficient that is typically between 0.5 and 1.0.

    Returns:
        float: The energy stored (in joules).
    """

    energy_stored = k * math.pow(light_intensity, n)
    return energy_stored

light_intensity = 100  # lux
k = 0.1  # constant value
n = 0.5  # coefficient value

energy_stored = calculate_energy_stored(light_intensity, k, n)
print("Energy stored:", energy_stored, "joules")
