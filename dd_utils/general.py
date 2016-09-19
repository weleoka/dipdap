"""
Utility module for DipDap.

Helper functions

	function readParameters(). 
		Reads flags/parameters from commandline,
		and modifies dipdap config dictionary accordingly.
    
    function clear_Screen(). 
        Clears the terminal window depending on operating system type.
"""

import os
import getopt
import logging
import logging.config
import dd_main.config

confRun = dd_main.config.run

def readParameters(argv):
    """ Commandline parameter parser.

    Function to parse parameters from commandline.

    parameters:
        argv: list. Command line flags and parameters.

    return:
        void
    """
    try:
        opts, args = getopt.getopt(argv,"hl:b:p:sv",["help", "lib=", "library=", "book=", "preview=", "subdirs", "version"])

    except getopt.GetoptError:
        print ("dipdap: unrecognized option.\nTry dipdap --help for more information.")
        print ("Invalid commandline option: %s"
            % str(argv))
        sys.exit(2)

    for opt, arg in opts:

        if opt in ("-h", "--help"):
            # https://groups.google.com/forum/#!topic/comp.lang.python/67A_BR3x-FU
            print (pydoc.render_doc(sys.modules[__name__]))
            sys.exit()

        elif opt in ("-v", "--verson"):
            print ("%s v.%s"
                % (confSys['name'], confSys['version']))
            print ("\tDeveloped by: %s.\n\n\tFor feature requests and praise ;P please send emails to:\n\t %s\n\n\tBug reporting to:\n\t %s\n\n\tPlease include 'dipdap' in subject header!\n\n"
                % (confSys['author'], confSys['author_email'], confSys['bug_reports']))            
            sys.exit(0)

        elif opt in ("-l", "--lib", "--library"):

            if check_user_input(arg, "dir"):
                confRun['root_dir'] = arg
                print ("found parameter 'library directory': %s"
                    % (arg))

        elif opt in ("-b", "--book"):

            if check_user_input(arg, "pass"):
                confRun['book_suffix'] = arg
                print ("found parameter 'book suffix': %s"
                    % (arg))

        elif opt in ("-p", "--preview"):

            if check_user_input(arg, "int"):
                confRun['book_preview'] = int(arg)
                print ("found parameter 'book preview length': %i"
                    % (int(arg)))

        elif opt in ("-s", "--subdirs"):
            confRun['subdirs'] = True

        else:
            print ("Running with default parameters.")

            return

    # Read from commandline file param or stdin. Could be interesting!
    # import fileinput # https://docs.python.org/2/library/fileinput.html
    # for line in fileinput.input():
    #    INPUT = line


def clear_screen():
    """ Clear the terminal window.

    Function to clear the terminal window.
    Different commands will be used depending on OS.

    #-> Interestingly prints '[3;J' and then clears terminal.

    parameters:
      void

    return:
      void
    """
    os.system('cls' if os.name == 'nt' else 'clear')