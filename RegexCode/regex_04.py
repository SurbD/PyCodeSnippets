import re

match_1 = re.sub(r'AB{3,6}?', '*', 'ABB ABBB ABBBB ABBBBBBB')
match_2 = re.sub(r'abc|xyz', '*', 'abcdefxyz123abc') # OR | 

# Matching only at the start and end
re_start = re.sub('^abc', '*', 'abcdefgabc')
re_end = re.sub('abc$', '*', 'abcdefgabc')

# <!-- To escape special characters use the backslash(\) eg. \+

print(re_start, re_end)