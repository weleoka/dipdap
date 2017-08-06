"""
Utility module for DipDap.

Database data processor.

Module handling the processes for sorting, validating and formatting db entries.

- Functions -
validate_data_in()
output_list_file()
prepare_db_entry()

"""

import re, sys, os
import dd_utils.filesystem
import dd_main.config


def validate_data_in(data_in, element_data):
    """
    Validation of form data. The current tests are:
        number      - pass if integer value.
        not-empty   - pass if not empty.
        datetime    - pass if conforms to datetime string rules.
        genre-valid - pass if valid genre.
        select-list - pass if in options list. Needs key param.
        form-key    - XSS preventor. Not operational.
        pass        - always pass.

    #-> If validating HTML elements the msg should be stored in dict
    #   with corresponding element id! Maybe outside of this function though.
    #-> datetime rule not ready.

    parameters:
        data_in: string. The input data.
        element_data: dict. All the elements data for parameters etc.

    return:
        boolean. True false if test passed or not.
        feedback: string. An error message.
    """
    validations = element_data.get('validation')
    element_attrs = element_data.get('attributes')
    nett_testing_result = True # Assumed not guilty until proven otherwise.
    feedback = ''
    msg =''

    for rule in validations:
        passed = True # Assumed not guilty until proven otherwise.

        if rule == 'number':
            # Should be in tuple (min, max) form.
            int_rng = element_attrs.get('range')

            try:
                sel = int(data_in)

                if int_rng:

                    if sel >= int_rng[0] and sel <= int_rng[1]:

                        continue # Continue to next rule in validations.

                    else:
                        passed, msg = False, "Number not in range."

            except ValueError:
                passed, msg = False, "Not a valid number"

        elif rule == 'not-empty':

            if data_in:

                continue # Continue to next rule in validations.

            else:
                passed, msg = False, "Please enter the information correctly."

        elif rule == 'select-list':
            # Should be in a list of tuples (x, y) form.
            options = element_attrs.get('options')
            
            try:
                i = int(data_in)
                doesindexexist = options[i]

            except TypeError:
                passed, msg = False, "Invalid option: 'not_a_number'"

            except IndexError:
                passed, msg = False, "Invalid option: 'out_of_range'"

            continue # Continue to next rule in validations.

        elif rule == 'datetime':

            continue # Continue to next rule in validations.

        elif rule == 'pass':

            continue # Continue to next rule in validations.

        if not passed:
            feedback += (" < %s > " % (msg))
            nett_testing_result = False

    return nett_testing_result, feedback


def output_list_file(db, list_file, sorting_option=None):
    """
    Create list file from DB

    db type is currently only CSV.

    #-> If db is empty then delete the newly created list file.
    #-> For each entry in db the list_file gets opened, writen to, and then closed.! This is due to repeated calls to append_to_file().

    parameters:
        db: string. The db file.
        list_file: string. The file to write the list to.
        (sorting_option: string. The method for sorting entries before writing.)

    return:
        void.

    """
    ticker = 0
    print("\nCompiling a human-readable, list of all entries in the index: %s \nWriting to file: %s"
        % (db, list_file))
    dataset = dd_utils.filesystem.read_library_file(db)

    if dataset is not None:

        for data_arr in dataset:
            ticker += 1
            entry = '\t\t'.join(data_arr)
            dd_utils.filesystem.append_to_file(entry, list_file)

        print("\n...Done! Total %i entries written to %s"
            % (ticker, list_file))

    else:
        print("The db seems to be empty.")


def prepare_db_entry(data_in):
    """
    Create entry from data.

    Data should include:
        Title
        Author
        Genre
        Genre2
        Date finished
        Score
        Comments

    Database type is currently only CSV.

    #-> The values have to be sorted according to configuration, this is currently read from config-file, but should perhapps be supplied as argument to make module re-usable.
    #-> What if the title of a book is an integer? There will be no apostrophies or quotation marks surrounding it!

    parameters:
        data_in: dictionary. Key - values pairs.

    return:
        csv_line: string. The new database entry.
    """
    arr = []
    database_type = dd_main.config.db['type']
    column_order = dd_main.config.db_csv_column_template

    if database_type == "csv":

        for (name, value) in data_in:
            try:
                i = column_order.index(name)

            except ValueError:
                raise ValueError("Element '%s' is not in db_csv_column_template."
                    % (name))

            try:
                int(value)
                arr.insert(i + 1, '%s, '
                    % (value))

            except ValueError:
                arr.insert(i + 1, '"%s", '
                    % (value))

        # Remove comma and whitespace from last list item. Append a newline char and then join the list into a nice string.
        arr[-1] = arr[-1].rstrip(', ')
        arr.append("\n")
        csv_line = ''.join(arr)

    elif database_type == "sql":
        print ("Not supported database type")
        sys.exit(1)

    return csv_line


