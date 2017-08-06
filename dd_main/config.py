""" Configuration file for dipdap and dipdap utilities package.

basic settings define general configuration and info. Use verbose or strict but not both.
    - name: program name.
    - version: program version.
    - author: developer name.
    - contributors: various people who have contributed to development.
    - author_email: developer email_in
    - bug_reports: bugg repport submissions.
    - logging_level: basic/advanced. This effects the logging module and sets handlers, filters and loggers.
        Recommended level is basic for the time being.
    - verbose: runs dipdap in verbose mode. Outputs full exception tracebacks etc.
    - strict: re-throws caught exceptions to halt execution.

run settings are what most users would modify with for example commandline arguments.
    - working_dir: Usually the folder where the script is executed.
    - default name for human readable dump of db entries.

run_db settings are for interacting with the database.
    - type: For example csv or postgresql. Currently only csv support.
    - name: the name of the file or the database in a db server deployment.
    - url: address to server
    - port: port to connect to.
    - user: username.
    - password: password.


db_csv_column_template - The column order of data in csv file.

dump_file_column_headers - Same as db_csv_column_template but for humans.
"""

basic = {
    'name': 'DipDap',
    'version': '0.0.1',
    'author': 'kawe0049',
    'contributors': '',
    'author_email': 'kawe0049@nonexcistent.yet',
    'bug_reports': 'kawe0049@nonexcistent.yet',
    'logging_level': 'basic', # Set to basic (later will include advanced which is not operational)
    'verbose': False,
    'strict': False
}

# Running configuration - change default running options here.
run = {
    'working_dir': '.'
}

db = {
    'type': 'csv',
    'url': None,
    'user': None,
    'password': None,
    'name': 'booklists.csv',
    'dump_file': 'library_dump.txt'
}

db_csv_column_template = ['title', 'author', 'genre', 'genre2', 'finish', 'score', 'comments']

dump_file_column_headers = "TITLE\t\tAUTHOR\t\tGENRE\t\tGENRE2\t\tFINISHED\t\tSCORE\t\tCOMMENTS\n"