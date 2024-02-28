import re
def text_match(text):
    x=re.split("_",text)
    ans=x[0]+''.join(y.title() for y in x[1:])
    return ans
a=input('')
print(text_match(a))