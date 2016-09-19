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

    #-> Need a way to sort the elements!
    #   Maybe have element_number instead of element_name.
    
    parameters:
        form_data: list. All the form data.
            [0] - submit action.
            [1] - method (GET/POST).
            [2] - elements data.

    return:
        html: string. All the form in one string.
    """
    elements = form_data[2]
    new_db_entry = []

    for element_name in elements:
        element_data = elements.get(element_name)
        element_label = element_data.get('label')
        attributes = element_data.get('attributes')
        validation = element_data.get('validation')
        element_name = attributes.get('name')
        validity = False
        msg = ''

        if attributes['type'] == 'text':

            while not validity:
                print(msg)
                data_in = input('%s: '
                    % (element_label))
                validity, msg = dd_utils.proc.validate_data_in(data_in, validation)

        elif attributes['type'] == 'select':
            opt_list = [] # Options list.
            options = attributes.get('options') # The raw data of options.
            i = 0 # Keep track of genre by list index! Could instead be line number, unique ID etc...
            tmp_genre_arr = [] # Keep track of main genres found.

            while i < len(options):
                genre, genre2 = options[i]
                i += 1

                # First instance of 'genre' found? Stick it in the opt_list alone!
                if genre not in tmp_genre_arr:
                    tmp_genre_arr.append(genre)
                    opt_list.append('\n') # Can't combine appends.. because? :)
                    opt_list.append(genre)

                ind = opt_list.index(genre) # Find index of main genre.

                tmp_opt_arr = ['\n\t\t[%i] %s' % (i, genre2)]

                opt_list.insert(ind + 1 , ''.join(tmp_opt_arr)) # Insert sub genre after main genre.

            print (''.join(opt_list))

            while not validity:
                print(msg)
                data_in = input('%s: '
                    % (element_label))
                validity, msg = dd_utils.proc.validate_data_in(data_in, validation, options)

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

