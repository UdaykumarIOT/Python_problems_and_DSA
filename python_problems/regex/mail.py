import re

s = 'k.paramaswaan12@gmail.com'
pattern = r'[\w_+*%-]+([\w_+*%-]*|\.+[\w_+*%-]+)@[\w-]+\.[a-zA-Z]{2,}'

res = re.fullmatch(pattern, s)
 
if res:
    print('Valid email address')
else:
    print('Invalid email address')