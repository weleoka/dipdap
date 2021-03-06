"""
Utility module for DipDap.

File system utility module for DipDap.

Module containing functions that access the local file system.
"""

import re, fnmatch, os

def check_file_status(destination, initial_line = ""):
    """
    Check status of a file, does it exist or not?
    If the file does not exist - create it. Optionally, in the code, with an inital legend.

    parameters:
        destination: string. the indexing file to check status of.
        initial_line: string. The first line of the new file. A legend, or some other text.

    return:
        boolean
    """

    if os.path.isfile(destination):

        while True:
            print("\nThe file being written to exists. What do you want to do?")
            print("\n[1] Append.")
            print("[2] Overwrite.")
            print("[9] Return to main menu.")
            option = input("Enter option: ")

            if option == "1": return True

            elif option == "2":

                while True:
                        y_n = input("Are you sure you want to overwrite the indexing file %s? y/n: "
                            % (destination))

                        if y_n in ['y', 'n']:

                                if y_n == 'y':
                                    myfile = open(destination, 'w')
                                    myfile.write(initial_line)
                                    myfile.close()

                                    return True

                                elif y_n == 'n':
                                    option = "9"

                                    break

            elif option == "9":
                print("\nReturned to main menu.\n")

                return False

    else:
        print("\nThe file - %s - could not be found... creating it."
            % (destination))
        myfile = open(destination, 'w')
        myfile.write(initial_line)
        myfile.close()

        return True


def check_path_status(path):
    """
    Check status of path to storage device.

    parameters:
        path: string. The directory path to check for validity.

    return:
        boolean
"""

    if os.path.exists(path):
        print("\nPath valid.\n")
        
        return True

    else:
        print("\nThe path %s appears to not exist. Sorry.\n"
            % (path))

        return False


def append_to_file(entry, destination):
    """
    Append to data to file.
    The open() function is used with the "a" for append argument.
    If the destination file does not exist python creates it.

    parameters:
        entry: string. An entry with file metadata to append to the indexing file
        destination: string. the indexing file to append the information to.

    return:
        void
    """
    print ("Entry: %s" % (entry))
    myfile = open(destination, 'a')
    myfile.write(str(entry))
    myfile.close()


def read_library_file(source):
    """
    Read the library db file line by line.
    
    Open file with r-tag for read only access.
    
    parameters:
        source: string. the indexing file to read information from.

    return:
        t: list. A list with nested lists of the entries.
    """
    t = []

    for line in open(source):    # open under default flag -r
        arr = []

        if line not in ['\n', '\r\n']: # Ignore empty lines.
            arr = re.split(', ', line)
             
        t.append(arr)

    return t



"""
    List comprehension way:
    t = [line.rstrip() for line in open(source)]

    line.rstrip
    option.isdigit()
    += augmented assignment
    use ; for one liners
    Y = X IF Z else W
    else in try while for loops

    for line in open(fff.txt)
"""