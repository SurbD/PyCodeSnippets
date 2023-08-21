import re

string = 'Locations L3 and D22 full'
# <!-- re.sub(pattern, replacement, string) -->
# print(re.sub(r'([a-zA-Z])(\d+)', '***', string))
# print(re.sub(r'([LRUD])(\d+)', '***', string))

# sub_ = re.sub('abc', '*', 'abcde abcxy') # replaces every occurence of 'abc'
sub_ = re.sub('[axc]', '*', 'abcde abcxy') # replaces occurence of every character in [] brackets
sub_ = re.sub('[abc][123]', '*', 'a1 + b3 + c2 + j2')
sub_ = re.sub('[a-jA-J][0-2]', '*', 'A1 + b3 + c2 + x2') # adding ranges with '-'
# print(sub_)

email_re = re.compile(r'^[a-zA-z][a-zA-Z0-9_.]+@(gmail)+\.[a-zA-Z]+$') # for only google mail (gmail), must start with letter
email_list = ['divinemukoro@gmail.com', 'surnb@mail.com', 'email.support@gmail.com', '121.adsa.com']

for email in email_list:
    if email_re.match(email):
        print(f'{email} --- Valid')

