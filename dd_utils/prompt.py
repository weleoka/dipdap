"""
Utility module for DipDap.

Prompt user for imput via commandline.

Functions for information data to stdout and take user input for processing.
"""
import dd_html.forms
import dd_utils.proc


def generate_form(form_data):
    """
    Generate a form which is filled in on the commandline.
    
    #-> Not DRY. The testing for imput validity repeats itself. Logic definitely be moved to validate_data_in()

    parameters:
        form_data: list. All the form data.
            [0] - submit action.
            [1] - method (GET/POST).
            [2] - elements data.

    return:
        html: string. All the form in one string.
    """
    i = 0
    elements = form_data[2]
    new_db_entry = []

    while i < len(elements):
        print (len(elements))
        i += 1
        
        # The solution for sorting the elements by incrementing name.
        element_data = elements['el-%s' % (i)]
        element_label = element_data.get('label')
        element_attrs = element_data.get('attributes')
        element_name = element_attrs.get('name')
        validity = False
        msg = ''
        feedback = ''

        if element_attrs['type'] in ['text', 'select', 'datetime', 'textfield']:
            att_type = element_attrs['type']
        
        else:

            raise ValueError('Incorrect element type: %s' % (element_attrs.get('type')))

        if att_type == 'text':

            while not validity:
                print(feedback)
                data_in = input(element_label)
                validity, feedback = dd_utils.proc.validate_data_in(
                    data_in,
                    element_data
                )

        elif att_type == 'select':
            opt_list = [] # Options list.
            options = element_attrs.get('options') # The raw data of options.
            j = 0 # Keep track of option by list index! Could instead be line number, unique ID etc...
            tmp_cat_arr = [] # Keep track of categories found.

            while j < len(options):
                cat, cat2 = options[j]
                
                # First instance of 'cat' found? Stick it in the opt_list alone!
                if cat not in tmp_cat_arr:
                    tmp_cat_arr.append(cat)
                    opt_list.append('\n') # Can't combine appends.. because? :)
                    opt_list.append(cat)

                tmp_opt_arr = ['\n\t\t[%i] %s' % (j, cat2)]

                ind = opt_list.index(cat) # Find index of main category.
                opt_list.insert(ind + 1 , ''.join(tmp_opt_arr)) # Insert sub cat after main cat.
                j += 1

            print (''.join(opt_list))

            while not validity:
                print(feedback)
                data_in = input(element_label)
                validity, feedback = dd_utils.proc.validate_data_in(
                    data_in,
                    element_data
                )
   
        # Add the (element_name, data) tuple to list.
        new_db_entry.append((element_name, data_in))

    return new_db_entry


def specify_db_file():
    """
    Promt user for database file path and name.

    parameters:
        void

    return:
        option: string. The option for menu navigation in main.
        db_file: string. The path and name of database file.
    """
    print("[1] Input name of custom database file.")
    print("[2] Return to main menu.")

    while True:
        option_02 = input('Enter option: ')

        if option_02 == "1":
            db_file = input('Enter filename: ')

        elif option_02 == "2":
            option = "refresh_menu"

            break

        else:
            print("\nDid not recognise the option: '%s'. Try again."
                % (option_02))

    return option, db_file


def get_main_menu():
    """
    Print main menu to stdout.

    parameters:
        void

    return:
        void
    """
    print("\n\t - DipDap -")
    print("[1] Add entry to database using terminal.")
    # Search by title
    # Start GUI (Add entry and search by title, also a quit button.)
    print("[2] Compile human readable file of entries already in database.")
    # Start socket server.
    print("[3] Output HTML form.")
    # Start CGI web server.
    print("[4] Print complete database to terminal.")
    print("[9] Quit.")

