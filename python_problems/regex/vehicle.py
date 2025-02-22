import re

s = 'TN23CA8451'
pattern = r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}'

res = re.fullmatch(pattern, s)
 
if res:
    print('Valid vehicle registration')
else:
    print('Invalid vehicle registration')