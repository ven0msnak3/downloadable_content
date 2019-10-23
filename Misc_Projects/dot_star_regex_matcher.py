import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Tarik Last Name: Sidiki')
mo.group(1)
mo.group(2)
