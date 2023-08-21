import re

pattern = re.compile(r'([a-zA-Z]).([a])')
pattern_2 = re.compile(r'^sea')
string = 'search this inside of this text please!, Andrei'

match_a = pattern.search(string)
match_b = pattern.findall(string)
match_c = pattern.fullmatch(string)
match_d = pattern.match(string)

a = pattern_2.split(string)
# print(match_object)
# print(dir(match_object))
print(pattern_2.findall(string))
print(match_b)

# Check out the website regex101.com