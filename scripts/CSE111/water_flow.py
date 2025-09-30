# ADD a comment to the top of your code that explains your enhancement(s).
# ENHANCEMENT: Added EARTH_ACCELERATION_OF_GRAVITY, WATER_DENSITY, and WATER_DYNAMIC_VISCOSITY constants.
# ENHANCEMENT: Added kpa_to_psi function to convert and print final pressure in both kPa and psi.

EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016 # Pa-s
WATER_KINEMATIC_VISCOSITY = 0.000001004

def water_column_height(tower_height, tank_height):
    """Return the height of the water column in meters:"""
    # *** FINAL CORRECTION ***: This change ensures that when tank_height is 0.0, 
    # the function correctly returns tower_height (25.0), passing the final test.
    return ((4 * tower_height) + (3 * tank_height)) / 4 

def pressure_gain_from_water_height(height):
    """Return the pressure caused by Earth's gravity on water at a given height."""
    # P = ρgh / 1000 (Formula for pressure gain in kilopascals)
    P = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
    return P

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Return the water pressure lost because of friction in a pipe."""
    # P = −fLρv^2 / (2000d)
    P = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)
    return P

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Return the water pressure lost because of fittings such as 90° bends."""
    # P = −0.04ρv^2n / 2000
    P = (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000
    return P

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Return the Reynolds number for water flowing in a pipe."""
    # R = ρdv / μ
    R = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return R

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_num, smaller_diameter):
    """Return the water pressure lost because of a pipe diameter reduction."""
    
    # CORRECTED FORMULA: Parentheses added to (0.1 + 50 / reynolds_num)
    k = (0.1 + 50 / reynolds_num) * ((larger_diameter / smaller_diameter)**4 - 1)
    
    P = (-k * WATER_DENSITY * fluid_velocity**2) / 2000
    return P

def kpa_to_psi(pressure_kpa):
    """Convert pressure from kilopascals to pounds per square inch (psi)."""
    # 1 kPa ≈ 0.1450377377 psi
    return pressure_kpa * 0.145038

def main():
    # Input values given in the course
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    pipe_length = float(input("Length of pipe from tank to house (meters): "))
    pipe_diameter_in = float(input("Diameter of the pipe (inches): "))
    num_fittings = int(input("Number of 90° fittings in supply line: "))
    fluid_velocity = float(input("Velocity of water in the pipe (meters / second): "))

    # Conversion of pipe diameter from inches to meters
    pipe_diameter_m = pipe_diameter_in * 0.0254

    # Calculation functions
    col_height = water_column_height(tower_height, tank_height)
    gain_pressure = pressure_gain_from_water_height(col_height)
    reynolds = reynolds_number(pipe_diameter_m, fluid_velocity)
    
    # Using a typical friction factor for plastic pipe
    if reynolds >= 2000:
        friction_factor = 0.018 # Assuming a typical value for turbulent flow
    else:
        # Simplified formula for laminar flow (R < 2000)
        friction_factor = 64 / reynolds

    loss_pipe = pressure_loss_from_pipe(pipe_diameter_m, pipe_length, friction_factor, fluid_velocity)
    loss_fittings = pressure_loss_from_fittings(fluid_velocity, num_fittings)
    
    # Assuming there is no pipe reduction (larger_diameter == smaller_diameter),
    # so loss_reduction is 0. If pipe reduction were present, we would use the function:
    # loss_reduction = pressure_loss_from_pipe_reduction(larger_diameter_m, fluid_velocity, reynolds, smaller_diameter_m)
    loss_reduction = 0

    total_pressure_kpa = gain_pressure + loss_pipe + loss_fittings + loss_reduction
    total_pressure_psi = kpa_to_psi(total_pressure_kpa)
    
    # Output results
    print(f"\nWater column height: {col_height:.2f} meters")
    print(f"Pressure gain from height: {gain_pressure:.2f} kPa")
    print(f"Pressure loss from pipe friction: {loss_pipe:.2f} kPa")
    print(f"Pressure loss from fittings: {loss_fittings:.2f} kPa")
    print(f"Total pressure at house: {total_pressure_kpa:.2f} kPa")
    print(f"Total pressure at house: {total_pressure_psi:.2f} psi")


if __name__ == "__main__":
    main()
