import re

s = '+91 8220664588'
pattern = r'\+91 [6-9]\d{9}'

res = re.fullmatch(pattern, s)
 
if res:
    print('Valid Indian mobile number')
else:
    print('Invalid Indian mobile number')