import re
def text_match(text):
    p='[A-Z]+[a-z]+$'
    if re.search(p,text):
        return 'Found a match!'
    else:
        return 'Not matched!'
a=input('')
print(text_match(a))