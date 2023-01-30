# Starting Out With Python 5th Edition: Chapter 5 - Exercise 14
# Main function
def main():
    # Input mass in kilograms of an object
    mass = get_mass()

    # Input velocity of an object
    velocity = get_velocity()

    # Calculate object's kinetic energy
    ke = kinetic_energy(mass, velocity)

    # Display object's kinetic energy
    display_ke(mass, velocity, ke)


# Function returns mass in kilograms of an object
def get_mass():
    mass = float(input('What is the mass in kilograms? '))
    while not(mass > 0):  # Input validation
        mass = float(input('Mass can\'t be negative, try again: '))
    return round(mass, 2)


# Function returns velocity of an object
def get_velocity():
    velocity = float(input('What is the velocity? '))
    return round(velocity, 2)


# Function displays the kinetic energy
def display_ke(m, v, ke):
    print('\nKE = (1/2) × ' + str(m) + ' × ' + str(v) + ' = ' + str(ke))


# Function calculates and returns the kinetic energy
def kinetic_energy(m, v):
    return (1/2)*m*(v**2)


# Call the main function
if __name__ == '__main__':
    main()
