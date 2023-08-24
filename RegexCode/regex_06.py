import re

# Groups
# <-- Using parentheses around part of an expression creates a group 
# that contains the text that matches a pattern -->

def modify(match):
    # The re.sub automatically sends a match object to the modify function
    letters = match.group()
    return letters.lower()

sub_ = re.sub(r'([A-Z])[a-z]', modify, 'PEACH Apple Apricot')
# print(sub_)


def modify_g(match):
    print(match.groups())
    letter, number = match.groups()
    return letter.lower() + str(int(number)+10)

g = re.sub(r'([A-Z])(\d)', modify_g, 'A1 + B2 + C4')
# print(g)

# <!-- Sub has an optional argument Count, which specifies 
# ...how many matches (from the left) to make-->

print(re.sub(r'a', '*', 'ababababa', count=3))

# findall - returns a list of all the matches found 
print(re.findall(r'[AB]\d', 'A3 + B2 + A9'))

# Split - is analogous to the string method, but allows us to 
# ...split on something more general then the string method does. -->
print(re.split(r'\+|\-', '3x+4y-12x^2+7'))

# Match and Search - are useful if you want to know if a match occurs 
# ...difference is match only check if the beginning of the string ...
# matches the pattern while search checks the entire string -->

if re.match(r'.com', 'johndoe@email.com'):
    print('Match found at the beginning!')
else:
    print('Not Match at beginning')

if re.search(r'.com', 'johndoe@email.com'):
    print('Match found in string!')
else:
    print('Not match Found')

# The Match object returned by the functions has group information in it

a = re.search(r'([ABC])(\d)', '= A3+B2+C8')
print(a.group())
print(a.group(1))
print(a.group(2))

# Remember re.search will only report the first match it finds in the string

# finditer
# returns an iterator of match ojects that we can loop through
for match_iter in re.finditer(r'([AB])(\d)', 'A3+B4'):
    print(match_iter.group(1))

# compile - Saves time if pattern is going to be reused

pattern = re.compile(r'[AB]\d')
print(pattern.sub('*', 'A3 + B4'))
print(pattern.sub('*', 'A8 + B9'))

# ---- When you compile an expression, for many of the methods you 
# can specify optional starting and ending indices in the string

pattern = re.compile('[AB]\d')
print(pattern.findall('A3+B4+C9+S2', 2, 6))