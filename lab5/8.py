import re
def text_match(text):
    x=re.findall('[A-Z][^A-Z]*',text)
    return x
a=input('')
print(text_match(a))