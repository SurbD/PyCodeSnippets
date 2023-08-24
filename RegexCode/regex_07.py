import re

#  <-- Roman Numerals - Using regular expressions
#  ...to convert roman numerals into ordinary numbers. -->

d = {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
      'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
}

pattern = re.compile(r"""(?x)
                    (M{0,3})(CM)?
                    (CD)?(D)?(C{0,3})
                    (XC)?(XL)?(L)?(X{0,3})
                    (IX)?(IV)?(V)?(I{0,3})""")

num = input('Enter Roman numeral: ').upper()
m = pattern.match(num)

sum = 0
print(m.groups())
print(m.group(), '--- Group Here')

for x in m.groups():
    # print('---', x)
    if x != None and x != '':
        if x in ['CM', 'CD', 'XC', 'XL', 'IX', 'IV']:
            sum += d[x]
        elif x[0] in 'MDCLXVI':
            sum += d[x[0]] * len(x)

print(sum)


# Dates --< Using regular expression to take a date in a format, like 
# ...'August 24, 2023' and convert it into an abbreviated format, 'mm/dd/yy' (with no leading Zeros) >--

d = {
    'jan': '1', 'feb': '2', 'mar': '3', 'apr': '4', 
    'may': '5', 'jun': '6', 'july': '7', 'aug': '8', 
    'sep': '9', 'oct': '10', 'nov': '11', 'dec': '12'
}

date = input('Enter date: ')
date_match = re.match(r'([A-Za-z]+)\.?\s*(\d{1,2}),?\s*(\d{4})', date)
print(f'{d[date_match.group(1).lower()[:3]]}/{date_match.group(2)}/{date_match.group(3)[-2:]}')
