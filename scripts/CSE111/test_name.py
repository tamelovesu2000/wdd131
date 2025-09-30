"""
water_flow.py
CSE 111 - Week 03 Project: Water Pressure

Enhancements:
1. Defined constants for gravity, water density, and viscosity instead of hardcoding.
2. Added a function to convert kPa to psi and print results in both units.
"""

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665        # m/s^2
WATER_DENSITY = 998.2                          # kg/m^3
WATER_DYNAMIC_VISCOSITY = 0.0010016            # Pa·s


def water_column_height(tower_height, tank_height):
    """Return the height of the water column in meters."""
    return tower_height + (3 * tank_height) / 4


def pressure_gain_from_water_height(height):
    """Return the pressure caused by Earth’s gravity on water at a given height."""
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Return the water pressure lost because of friction in a pipe."""
    return (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)


def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Return the water pressure lost because of fittings such as 90° bends."""
    return (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000


def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Return the Reynolds number for water flowing in a pipe."""
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_num, smaller_diameter):
    """Return the water pressure lost because of a pipe diameter reduction."""
    k = 0.1 + (50 / reynolds_num) * ((larger_diameter / smaller_diameter)**4 - 1)
    return (-k * WATER_DENSITY * fluid_velocity**2) / 2000


def kpa_to_psi(pressure_kpa):
    """Convert pressure from kilopascals to pounds per square inch (psi)."""
    return pressure_kpa * 0.145038


def main():
    # Input values
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    pipe_length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    num_fittings = int(input("Number of 90° angles in supply pipe: "))
    pipe_length2 = float(input("Length of pipe from supply to house (meters): "))

    # Assumptions given in the course
    pipe_diameter1 = 0.28687    # meters
    pipe_diameter2 = 0.048692   # meters
    friction_factor = 0.013
    fluid_velocity = 1.65

    # Calculations
    h = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(h)
    pressure += pressure_loss_from_pipe(pipe_diameter1, pipe_length1, friction_factor, fluid_velocity)
    pressure += pressure_loss_from_fittings(fluid_velocity, num_fittings)
    reynolds = reynolds_number(pipe_diameter1, fluid_velocity)
    pressure += pressure_loss_from_pipe_reduction(pipe_diameter1, fluid_velocity, reynolds, pipe_diameter2)
    pressure += pressure_loss_from_pipe(pipe_diameter2, pipe_length2, friction_factor, fluid_velocity)

    # Output in both kPa and psi
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.1f} psi")


if __name__ == "__main__":
    main()
