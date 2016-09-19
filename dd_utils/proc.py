"""
Utility module for DipDap.

Database data processor.

Module handling the processes for sorting, validating and formatting db entries.

- Functions -
validate_data_in()
output_list_file()
create_db_entry()

"""

import re, sys, os
import dd_utils.filesystem


def validate_data_in(data_in, validations, key=None):
    """
    Validation of form data. The current tests are:
        number      - pass if integer value.
        not-empty   - pass if not empty.
        date        - pass if conforms to date string.
        genre-valid - pass if valid genre.
        select-list - pass if in options list. Needs key param.
        form-key    - XSS preventor. Not operational.
        pass        - always pass.

    #-> If validating HTML elements the msg should be stored in dict
    #   with corresponding element id! Maybe outside of this function though.
    #-> Multiple tests for one element all need to be run!

    parameters:
        data_in: string. The input data.
        validations: list. The validation criteria.
        key: list. Other data such as:
            - form key [random 64-character string]
            - select options. Does the options list have the index specified.
            - number ranges [min, max]

    return:
        boolean. True false if test passed or not.
        message: string. An error message.
    """
    msg =''

    if 'number' in validations:

        try:
            int(data_in)

        except ValueError:

            return False, "Not a valid number"

        if key:

            if data_in >= key[0] and data_in <= key[1]:

                pass

            else:

                return False, "Number not in range."

    if 'not-empty' in validations:

        if data_in:

            pass

        else:

            return False, "Please enter the information correctly."

    if 'select-list' in validations:

        try:
            i = int(data_in)

        except TypeError:

            return False, "Invalid option: 'not_a_number'"

        try:
            doesindexexist=key[i]

        except IndexError:

            return False, "Invalid option: 'out_of_range'"

    if 'pass' in validations:
        msg = "Cleared with 'pass' validation."

    return True, msg


def output_list_file(db, list_file, sorting_option=None):
    """
    Create list file from DB

    db type is currently only CSV.

    #-> If db is empty then delete the newly created list file.

    parameters:
        db: string The db file.
        list_file: string. The file to write the list to.
        DISABLED sorting_option: string. The method for sorting entries before writing.

    return:
        void.

    """
    ticker = 0
    print("\nCompiling a human-readable, list of all entries in the index: %s \nWriting to file: %s"
        % (db, list_file))
    dataset = dd_utils.filesystem.read_library_file(db)
    
    if dataset is not None:
        for entry in entries:
            ticker += ticker
            dd_utils.filesystem.append_to_file(entry, list_file)

        print("\n...Done! Total %i entries written to %s"
            % (ticker, list_file))
        sleep(4)

    else:
        print("The db seems to be empty.")

        pass


def create_db_entry(data_in, database_type):
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

    parameters:
        data_in: dictionary. Key - values pairs.
        database_type: string. The type of database to prepare new entry for.

    return:
        entry: string. The new database entry.
    """

    if database_type == "csv":
       print(data_in)

    elif database_type == "sql":
        print ("Not supported database type")
        sys.exit(1)



