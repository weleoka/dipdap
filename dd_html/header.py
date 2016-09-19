"""
HTML header generation functions.
"""


def get_header():
    """
    Generate an HTML5 header.

    parameters:
		Void

    return:
        html: string. All the header in one string.
    """
    return '''
<!doctype html>
<html lang="en">

<!-- Header -->
<head>
  <meta charset="utf-8">
	<title> This is the title </title>
	
	<!-- links to external stylesheets -->	
	<link rel="stylesheet" href="style/stylesheet.css" title="General stylesheet">

	
	<!-- favicon -->
	<link rel="shortcut icon" href="img/drop.png">
</head>
<body> 
'''