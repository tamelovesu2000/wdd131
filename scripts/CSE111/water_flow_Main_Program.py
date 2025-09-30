"""
W03 Project: Water Pressure
Enhancements:
1. Added constants for gravity, density, and viscosity.
2. Added a function to convert kPa to psi.
"""

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665     # m/s²
WATER_DENSITY = 998.2                       # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016         # Pa·s

def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height / 4)

def pressure_gain_from_water_height(height):
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    return (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    return (-k * WATER_DENSITY * fluid_velocity**2) / 2000

def kpa_to_psi(kpa):
    return kpa * 0.145038

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    supply_length = float(input("Length of supply pipe from tank to lot (meters): "))
    fittings = int(input("Number of 90° angles in supply pipe: "))
    house_length = float(input("Length of pipe from supply to house (meters): "))

    # Calculate
    h = water_column_height(tower_height, tank_height)
    p = pressure_gain_from_water_height(h)
    p += pressure_loss_from_pipe(0.28687, supply_length, 0.013, 1.65)
    p += pressure_loss_from_fittings(1.65, fittings)
    p += pressure_loss_from_pipe(0.022092, house_length, 0.013, 1.65)

    print(f"Pressure at house: {p:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(p):.1f} psi")

if __name__ == "__main__":
    main()
