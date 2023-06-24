str = ""
while True:
    try:
        str += input().lower() + "   "
    except EOFError:
        break
text = str.replace('?', '.').replace('!', '.').split('.')
for i in text:
    s = " ".join(i.split())
    print(s[0:1].upper() + s[1:])