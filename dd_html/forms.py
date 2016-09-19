"""
HTML Utility module for DipDap.

Module handling the processes of making forms.

make_form()
"""

import dd_html.elements


def make_form(form_data):
    """
    Generate an HTML5 form.

    #-> Need a way to sort the elements!
    #   Maybe have element number instead of name.

    parameters:
        form_data: list. All the form data.
            [0] - submit action.
            [1] - method (GET/POST).
            [2] - elements data.

    return:
        html: string. All the form in one string.
    """
    action = form_data[0]
    method = form_data[1]
    elements = form_data[2]

    form_html = ['\n<form action="%s" method="%s">' % (action, method)]


    for element_name in elements:
        element_data = elements.get(element_name)
        element_label = element_data.get('label')
        attributes = element_data.get('attributes')
        element_id = attributes.get('id')
        element_html = ['\n\t<label for="%s">%s</label>' % (element_id, element_label)]

        if attributes['type'] == 'text':
            element_html.append('\n\t<input ')
            element_html += dd_html.elements.get_header(attributes)
            element_html.append('/>\n') # Close the element.

        elif attributes['type'] == 'select':
            element_html.append('\n\t<select ')
            element_html += dd_html.elements.get_header(attributes)
            element_html += dd_html.elements.gen_select_options_from_list(attributes) # Combine with options list.
            element_html.append('\t</select>\n') # Close the element.

        # If there are any relevant messages regarding element attatch them.
        element_html.append(element_data['messages'])
        form_html += element_html # Add the new element to form.

    form_html.append('\n</form>') # Elements finished, close form.

    print(form_html[139])

    try:
        stringed = ''.join(form_html)

    except TypeError as e:
        
        raise e

    return stringed # And... then it is magically all valid HTML!

