""" A script for units of a length """

# Main unit function
def length_unit():
    print('Available units:\n\t1. cm\n\t2. m\n\t3. km')
    options = ['1', '2', '3']
    choice = None

    while choice not in options:
        choice = input("Pick any unit above(1-3): ")

    if choice == '1':
        units = 'cm'
    elif choice == '2':
        units = 'm'
    else:
        units = 'km'

    return units
