#! /usr/bin/python3

# Opens browser from your saved home location in google to user entered address
# Assumes user is logged into a google account with a saved home address

import webbrowser, sys

# If an address is entered save that to navTo variable
if len(sys.argv)>1:

	navTo = ' '.join(sys.argv[1:])

# If no address entered notify user and exit
else:

	print('Enter Where your are coming from and going to')
	sys.exit()

# Opens webbrowser to desired location
webbrowser.open('https://www.google.com/maps/dir/Home/'+navTo)
