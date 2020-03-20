#!/usr/local/bin/python3
#print("Content-Type: text/html")    
#print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
name = form.getvalue('fname')
print("Name of our user is:",name)