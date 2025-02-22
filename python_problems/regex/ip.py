import re

s = '127.0.0.1'

pattern = r'(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])(\.(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])){3}'

res = re.fullmatch(pattern, s) 

if res:
    print('Valid IP address')
else:
    print('Invalid IP address')