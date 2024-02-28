import re
def text_match(text):
    x=re.sub("[ ,.]",":",text)
    return x
a=input('')
print(text_match(a))