#!/usr/bin/python

# Imports
from datetime import datetime
import re
import calendar
import math
import random

# Set variables
characters = ['a''b''c''d''e''f''g''h''i''j''k''l''m''n''o''p''q''r''t''u''v''w''x''y''z']
numbers = ['1''2''3''4''5''6''7''8''9''10''11''12''13''14''15''16''17''18''19''20''21''22''23''24']
debug = 0
value = 0
list = []
output = []
password = []
qual = 0

# Get password length from user
while (qual != 1):
    passlength = input("[QUERY] How long would you like your password to be?: ")
    try:
        val = int(passlength)
        qual = 1
    except ValueError:
        print("[ERROR] Must be an integer. Try again! \n")
    
print("\n")

# Get the current time and set to dt1
d = datetime.utcnow()

# Print datetime
if (debug == 1):
    print ("[DEBUG] Datetime: ", d)

# Convert datetime to timestamp
dt2 = calendar.timegm(d.utctimetuple())

# Print out the current timestamp
if (debug == 1):
    print ("[DEBUG] Current timestamp: ", dt2)

# Get the hostname
hostname = input("[QUERY] Please enter the hostname of the device: ")
if (debug == 1):
    print ("[DEBUG] The hostname you entered is: ", hostname)

# # Convert hostname to lowercase
# hostname = hostname.lower()
# if (debug == 1):
    # print ("[DEBUG] Hostname lowercase is: ", hostname)


# Convert
for character in hostname:
    number = ord(character)
    output.append(number)
if (debug == 1):
    print ("[DEBUG] Output is currently: ", output)
asciihostname = ''.join(str(e) for e in output)
    
# Print the hostname in numbers
if (debug == 1):
    print ("[DEBUG] Ascii Hostname is: ", asciihostname)

# Math time*serverascii into password base value
pbv = int(asciihostname) * int(dt2)

# Print PBV
if (debug == 1):
    print ("[DEBUG] The password base value is: ", pbv)
    
# Get the iteration
digits = int(math.log10(pbv)) + 1

# Print Digits
if (debug == 1):
    print ("[DEBUG] The digit is: ", digits)

# Set the random point
point = random.randint(0,digits-2) #Inclusive

# Print the random number
if (debug == 1):
    print ("[DEBUG] random number is: " , point)



# WHILE Passwordlength < wantedlength

# # # Find point in int and assign it to charval
Password_string = str(pbv)
charval = Password_string[point]
list.append(charval)
intcharval = ''.join(str(e) for e in list)

if (debug == 1):
    print ("[DEBUG] Character value is: " , charval)

# # # Check if charval is > 33 and < 128
while (value != int(passlength)):
    if (debug == 1):
        print("[DEBUG] passlength is : " , passlength)
        print("[DEBUG] value is : " , value)
    intcharval = ''.join(str(e) for e in list)
    if 33 < int(intcharval) < 126:
# # If so
# # # Convert to ASCII
        Pchar = chr(int(intcharval))
        password.append(Pchar)
        PasswordValue = ''.join(str(e) for e in password)
        if (debug == 1):
            print("[DEBUG] Password currently: ", PasswordValue)
        value = value + 1
        point = random.randint(0,digits-2)
        list = []
        if (debug == 1):
            print("[DEBUG] Point after step: ", point)
        charval = Password_string[point]
        list.append(charval)
        
    else:
        if 2 == int(intcharval):
            if (debug == 1):
                print("[DEBUG] Point before step: ", point)
            point = random.randint(0,digits-2)
            list = []
            if (debug == 1):
                print("[DEBUG] Point after step: ", point)
            charval = Password_string[point]
            list.append(charval)
            if (debug == 1):
                print("[DEBUG] ", list)
        if  126 < int(intcharval):
            if (debug == 1):
                print("[DEBUG] Point before step: ", point)
            point = random.randint(0,digits-2)
            list = []
            if (debug == 1):
                print("[DEBUG] Point after step: ", point)
            charval = Password_string[point]
            list.append(charval)
            if (debug == 1):
                print("[DEBUG] ", list)
        else:
            if (debug == 1):
                print("[DEBUG] Point before step: ", point)
            point = point + 1
            if  point == digits:
                if (debug == 1):
                    print("[DEBUG] Point before step: ", point)
                point = random.randint(0,digits-2)
                list = []
                if (debug == 1):
                    print("[DEBUG] Point after step: ", point)
                charval = Password_string[point]
                list.append(charval)
                if (debug == 1):
                    print("[DEBUG] ", list)
            else:
                if (debug == 1):
                    print("[DEBUG] Point after step: ", point)
                charval = Password_string[point]
                list.append(charval)
                if (debug == 1):
                    print("[DEBUG] ", list)
            #list.append(Password_string[point])
if (debug == 1):
    print("[DEBUG] char val is: " , intcharval)
print ("[INFO] Your password is: ", PasswordValue)
        
        
# # Else

# # # Increase point by 1 in int

# # ## Append value to charval




