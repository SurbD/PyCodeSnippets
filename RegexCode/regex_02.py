import re

email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = 'divine@gmail.com'

match = email_pattern.match(email)
print(match.pos)
print(match)