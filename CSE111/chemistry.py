from formula import parse_formula

# Define the make_periodic_table function
def make_periodic_table():
    periodic_table_dict = {
        "H": ["Hydrogen", 1.00794],
        "He": ["Helium", 4.002602],
        "Li": ["Lithium", 6.941],
        "Be": ["Beryllium", 9.012182],
        "B": ["Boron", 10.811],
        "C": ["Carbon", 12.0107],
        "N": ["Nitrogen", 14.0067],
        "O": ["Oxygen", 15.9994],
        "F": ["Fluorine", 18.9984032],
        "Ne": ["Neon", 20.1797],
        "Na": ["Sodium", 22.98976928],
        "Mg": ["Magnesium", 24.305],
        "Al": ["Aluminum", 26.9815386],
        "Si": ["Silicon", 28.0855],
        "P": ["Phosphorus", 30.973762],
        "S": ["Sulfur", 32.065],
        "Cl": ["Chlorine", 35.453],
        "K": ["Potassium", 39.0983],
        "Ar": ["Argon", 39.948],
        "Ca": ["Calcium", 40.078],
        "Sc": ["Scandium", 44.955912],
        "Ti": ["Titanium", 47.867],
        "V": ["Vanadium", 50.9415],
        "Cr": ["Chromium", 51.9961],
        "Mn": ["Manganese", 54.938045],
        "Fe": ["Iron", 55.845],
        "Co": ["Cobalt", 58.933195],
        "Ni": ["Nickel", 58.6934],
        "Cu": ["Copper", 63.546],
        "Zn": ["Zinc", 65.38],
        "Ga": ["Gallium", 69.723],
        "Ge": ["Germanium", 72.64],
        "As": ["Arsenic", 74.9216],
        "Se": ["Selenium", 78.96],
        "Br": ["Bromine", 79.904],
        "Kr": ["Krypton", 83.798],
        "Rb": ["Rubidium", 85.4678],
        "Sr": ["Strontium", 87.62],
        "Y": ["Yttrium", 88.90585],
        "Zr": ["Zirconium", 91.224],
        "Nb": ["Niobium", 92.90638],
        "Mo": ["Molybdenum", 95.96],
        "Tc": ["Technetium", 98],
        "Ru": ["Ruthenium", 101.07],
        "Rh": ["Rhodium", 102.9055],
        "Pd": ["Palladium", 106.42],
        "Ag": ["Silver", 107.8682],
        "Cd": ["Cadmium", 112.411],
        "In": ["Indium", 114.818],
        "Sn": ["Tin", 118.71],
        "Sb": ["Antimony", 121.76],
        "I": ["Iodine", 126.90447],
        "Te": ["Tellurium", 127.6],
        "Xe": ["Xenon", 131.293],
        "Cs": ["Cesium", 132.9054519],
        "Ba": ["Barium", 137.327],
        "La": ["Lanthanum", 138.90547],
        "Ce": ["Cerium", 140.116],
        "Pr": ["Praseodymium", 140.90765],
        "Nd": ["Neodymium", 144.242],
        "Pm": ["Promethium", 145],
        "Sm": ["Samarium", 150.36],
        "Eu": ["Europium", 151.964],
        "Gd": ["Gadolinium", 157.25],
        "Tb": ["Terbium", 158.92535],
        "Dy": ["Dysprosium", 162.5],
        "Ho": ["Holmium", 164.93032],
        "Er": ["Erbium", 167.259],
        "Tm": ["Thulium", 168.93421],
        "Yb": ["Ytterbium", 173.054],
        "Lu": ["Lutetium", 174.9668],
        "Hf": ["Hafnium", 178.49],
        "Ta": ["Tantalum", 180.94788],
        "W": ["Tungsten", 183.84],
        "Re": ["Rhenium", 186.207],
        "Os": ["Osmium", 190.23],
        "Ir": ["Iridium", 192.217],
        "Pt": ["Platinum", 195.084],
        "Au": ["Gold", 196.966569],
        "Hg": ["Mercury", 200.59],
        "Tl": ["Thallium", 204.3833],
        "Pb": ["Lead", 207.2],
        "Bi": ["Bismuth", 208.9804],
        "Po": ["Polonium", 209],
        "At": ["Astatine", 210],
        "Rn": ["Radon", 222],
        "Fr": ["Francium", 223],
        "Ra": ["Radium", 226],
        "Ac": ["Actinium", 227],
        "Th": ["Thorium", 232.03806],
        "Pa": ["Protactinium", 231.03588],
        "U": ["Uranium", 238.02891],
        "Np": ["Neptunium", 237],
        "Pu": ["Plutonium", 244],
        "Am": ["Americium", 243],
        "Cm": ["Curium", 247],
        "Bk": ["Berkelium", 247],
        "Cf": ["Californium", 251],
        "Es": ["Einsteinium", 252],
        "Fm": ["Fermium", 257],
        "Md": ["Mendelevium", 258],
        "No": ["Nobelium", 259],
        "Lr": ["Lawrencium", 262],
        "Rf": ["Rutherfordium", 267],
        "Db": ["Dubnium", 270],
        "Sg": ["Seaborgium", 271],
        "Bh": ["Bohrium", 270],
        "Hs": ["Hassium", 277],
        "Mt": ["Meitnerium", 276],
        "Ds": ["Darmstadtium", 281],
        "Rg": ["Roentgenium", 282],
        "Cn": ["Copernicium", 285],
        "Nh": ["Nihonium", 286],
        "Fl": ["Flerovium", 289],
        "Mc": ["Moscovium", 290],
        "Lv": ["Livermorium", 293],
        "Ts": ["Tennessine", 294],
        "Og": ["Oganesson", 294],
    }
    return periodic_table_dict

# Define the compute_molar_mass function
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    """
    total_molar_mass = 0.0
    for symbol, quantity in symbol_quantity_list:
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass

# Define the main function
def main():
    # Get a chemical formula for a molecule from the user.
    formula = input("Enter the molecular formula of the sample: ")

    # Get the mass of a chemical sample in grams from the user.
    mass_in_grams = float(input("Enter the mass in grams of the sample: "))

    # Call the make_periodic_table function and store the periodic table in a variable.
    periodic_table = make_periodic_table()

    # Call the parse_formula function to convert the chemical formula given by the user
    # to a compound list that stores element symbols and the quantity of atoms of each
    # element in the molecule.
    symbol_quantity_list = parse_formula(formula, periodic_table)

    # Call the compute_molar_mass function to compute the molar mass of the molecule
    # from the compound list.
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    # Compute the number of moles in the sample.
    number_of_moles = mass_in_grams / molar_mass

    # Print the molar mass.
    print(f"{molar_mass:.5f} grams/mole")

    # Print the number of moles.
    print(f"{number_of_moles:.5f} moles")

if __name__ == "__main__":
    main()
