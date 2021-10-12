import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
indian no. +91 5588-940010
indian no. ++91 5588-000000

bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''


# item = re.compile(r'..ai')       # '.': Matches any single character except newline
# item = re.compile()

# item = re.compile(r'iiii$')     # $ Ends with

# item = re.compile(r'ai*')       # * Zero or more occurrences

# item = re.compile(r'www+')      # + One or more occurrences

# item = re.compile(r'ai{2}')     # {} Exactly the specified number of occurrences

# item = re.compile(r'(ai){1}')   # () Capture and group

# item = re.compile(r'^Tata')     # ^ Starts with

# item = re.compile(r'ai|Tata|www')     # | Either or



# Special sequence

# item = re.compile(r'\ATata')        # \A Returns a match if the specified characters are at the beginning of the string

# item = re.compile(r'\bPhone')        # \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"

# item = re.compile(r'com\b')        # \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"

# item = re.compile(r'\d{5}-\d{4}')     # \d Returns a match where the string contains digits (numbers from 0-9)

# item = re.compile(r'iiii\Z')        # \Z Returns a match if the specified characters are at the end of the string



# item = re.compile(r'.\b91 \d{4}-\d{6}')
item = re.compile(r'\W{1}91 \d{4}-\d{6}|\W{2}91 \d{4}-\d{6}')

item_1 = item.finditer(mystr)
for text in item_1:
    print(text)