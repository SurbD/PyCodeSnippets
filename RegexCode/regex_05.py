import re 

# <!-- Backslash Sequences -->

# <-- "\d" matches any digit, "\D" matches any Non-digits -->
d = re.sub(r'\d', '*', '3 + 14 = 17')
D = re.sub(r'\D', '*', '3 + 14 = 17')

# <-- "\w" matches any letter or number, "\W" matches anythin else -->
w = re.sub(r'\w', '*', 'This is a test. Or is it?')
W = re.sub(r'\W', '*', 'This is a test. Or is it?')

# <-- "\s" matches whitespace, "\S" matches non-whitespace -->
s = re.sub(r'\s', '*', 'This is a test. Or is it?')
S = re.sub(r'\S', '*', 'This is a test. Or is it?')
# print(s, '----', S)

# <!-- Preceding and following slashes -->

thecat = re.sub(r'(?<=d )the(?= cat)', '*', 'the dog and the cat tried')
match_the = re.sub(r'(?<!\w)[Tt]he(?!\w)', '*', 'The cat is on the lathe there')
# print(match_the)

#  <!-- Flags -->
# (?i) - Ignore Case
# (?s) - Match Newline

ignore = re.sub('(?i)ab(?!\w)', '*', 'ab AB about aB Ab')

# (?x) - For More verbose Multi-line format, whitespace are ignored + commments allowed
# pattern = r'(?x)[AB]\d+|[CD]\d+'
pattern = r"""(?x) [AB]\d+ # Match A or B followed by some digits
                  [CD]\d+ # Match C or D followed by some digits
"""

print(re.sub(pattern, '*', 'A3C9 and C1B17'))


# print(ignore)