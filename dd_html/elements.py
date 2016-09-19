"""
Utility module for DipDap.
HTML elements module

Module handling the processes of making elements.

gen_select_options_from_list()
gen_select_options_from_dict()
get_header()

#-> Combine the two select_op_list generators into one which tests the input data.
"""


def gen_select_options_from_list(attributes):
    """
    Generate the options list for a select dropdown list.

    Two tiers deep, so two layer of options with dependencies..

    parameters:
        attributes: dict. All the emlements attributes.

    return:
        opt_html: list. All the options in HTML strings in a list.
    """
    opt_html = [] # Options list with HTML code
    options = attributes.get('options') # The raw data of options.
    i = 0 # Keep track of genre by list index! Could instead be line number, unique ID etc...
    tmp_genre_arr = [] # Keep track of main genres found.

    while i < len(options):
        genre, genre2 = options[i]
        i += 1

        # First instance of 'genre' found? Stick it in the html list alone!
        if genre not in tmp_genre_arr:
            tmp_genre_arr.append(genre)
            opt_html.append('\n') # Can't combine appends.. because? :)
            opt_html.append(genre)

        ind = opt_html.index(genre) # Find index of main genre.

        tmp_opt_arr = ['\n\t\t<option value="%i"' % (i)]

        if attributes.get('value') == i:
            tmp_opt_arr.append(' selected')

        tmp_opt_arr.append('>%s</option>' % (genre2))

        opt_html.insert(ind + 1 , ''.join(tmp_opt_arr)) # Insert sub genre after main genre.

    return ''.join(opt_html)


def gen_select_options_from_dict(attributes):
    """
    Generate the options list for a select dropdown list.

    One tier deep, so single layer of options all independent.

    parameters:
        attributes: dict. All the emlements attributes.

    return:
        opt_html: list. All the options in HTML strings in a list.
    """
    opt_html = [] # Make options list
    options = attributes.get('options')

    for optValue, optText in options.items():
        opt_html.append('\t\t<option value="%s"' % (optValue))

        if attributes.get('value') == optValue:
            opt_html.append(' selected')

        opt_html.append('>%s</option>\n' % (optText))

    return opt_html


def get_header(attributes):
    """
    Generate an HTML5 element header.

    The element header are all the attributes enclosed in < and />.

    parameters:
        attributes: dict. All the emlements attributes.

    return:
        header: list. All the attributes in HTML strings in a list.
    """
    header =[]

    for attribute, value in attributes.items():

        if attribute == 'options':

            continue

        header.append('%s="%s" ' % (attribute, value))

    return ''.join(header)