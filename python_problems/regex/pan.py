import re

s='AGIRK4982A'
pattern = r'[A-Z]{5}\d{4}[A-Z]{1}'

res = re.fullmatch(pattern,s)

if res:
    print('Valid pan card')
else:
    print('Invalid pan card')