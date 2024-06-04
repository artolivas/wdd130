# water_flow.py

# Constants
WATER_DENSITY = 998.2  # kg/m^3
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s^2
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pascal seconds

def water_column_height(tower_height, tank_height):
    """
    Calculate and return the height of a column of water.

    Parameters:
        tower_height: the height of the tower (float)
        tank_height: the height of the walls of the tank (float)

    Return:
        The height of the water column (float)
    """
    return tower_height + (3 / 4) * tank_height

def pressure_gain_from_water_height(height):
    """
    Calculate and return the pressure gain from water height.

    Parameters:
        height: the height of the water column (float)

    Return:
        The pressure gain in kilopascals (float)
    """
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate and return the pressure loss from a pipe.

    Parameters:
        pipe_diameter: diameter of the pipe (float)
        pipe_length: length of the pipe (float)
        friction_factor: friction factor of the pipe (float)
        fluid_velocity: velocity of the fluid in the pipe (float)

    Return:
        The pressure loss in kilopascals (float)
    """
    return (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate the water pressure lost because of fittings in a pipeline.

    Parameters:
        fluid_velocity: the velocity of the water (float)
        quantity_fittings: the number of fittings (int)

    Return:
        The pressure loss in kilopascals (float)
    """
    return (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculate and return the Reynolds number.

    Parameters:
        hydraulic_diameter: the diameter of the pipe (float)
        fluid_velocity: the velocity of the water (float)

    Return:
        The Reynolds number (float)
    """
    return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculate the water pressure lost because of a reduction in pipe diameter.

    Parameters:
        larger_diameter: the diameter of the larger pipe (float)
        fluid_velocity: the velocity of the water (float)
        reynolds_number: the Reynolds number (float)
        smaller_diameter: the diameter of the smaller pipe (float)

    Return:
        The pressure loss in kilopascals (float)
    """
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    return (-k * WATER_DENSITY * fluid_velocity**2) / 2000

# Constants for PVC and HDPE pipes
PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013  # unitless
SUPPLY_VELOCITY = 1.65  # meters / second

HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018  # unitless
HOUSEHOLD_VELOCITY = 1.75  # meters / second

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()
