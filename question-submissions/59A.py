element = input()
if len([x for x in element if x.isupper()])>len(element)/2:
    print(element.upper())
else:
    print(element.lower())