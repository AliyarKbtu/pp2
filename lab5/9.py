import re
def text_match(text):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", text)
a=input('')
print(text_match(a))