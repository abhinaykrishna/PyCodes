import re 

# search and sub are manily used for searching and substitution 
# None will be returned if not found

# Metachars
# . - Used to match one occurrence of any character
# \d - Used to match one occurrence of any digit from 0-9
# * - Used to match zero or more occurrences of previous character
# + - Used to match one or more occurrences of previous character
# ? - Used to match zero or one occurrence of previous character
# {} - Used to match exactly n occurrences of previous character
# [] - Used to match one occurrence of any characters present within square brackets
# ^ - Used to match a pattern at the beginning of a string
# $ - Used to match a pattern at the end of a string
# \w - Used to match an word character which includes alphabets(a-zA-Z), digits(0-9) and '_'
# \s-  Used to match single space or sequence of spaces (including \t \n)
# | - Used to match any one pattern which is on either side of it

# To search the pattern having two characters in between A and l in the given string "Aopline".

if(re.search(r"A..l","Aopline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# To search for a digit between A and l in the given string "A2line".

if(re.search(r"A\dl","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# To check if a number is found 0 or n times after A in the given string.

if(re.search(r"A\d*","A2234line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# To check if a number is found 1 or n times after A in the given string.

if(re.search(r"A\d+","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# To check if a number is found 0 or 1 times after A in the given string.

if(re.search(r"A\d?i","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# To search for a number between 4 and 8 in between A and l in the given string.

if(re.search(r"A[4-8]l","A2line")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# To check if the given string is starting with A.

if(re.search(r"^A","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# To check if the given string is ending with e.

if(re.search(r"e$","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# To check whether last character is alphanumeric or not.

if(re.search(r"\w$","Airline%")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# To check for the space after "Air" in the given string "Airline".

if(re.search(r"Air\s","Airline")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# To search for the pattern "Hell" or "Fell" in the given string "Fellow".

if(re.search(r"Hell|Fell","Fellow")!=None):
    print("Pattern found")
else:
    print("Pattern not found")

# Substitution
flight_details="Flight Savana Airlines a2134"
print(flight_details)
print(re.sub(r"Flight",r"Plane",flight_details))