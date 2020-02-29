import re

match = re.search(r'[1-9]\d{5}', "BIT 100081 10082")
if match:
    print(match.group(0))

match = re.match(r'[1-9]\d{5}', "100081 BIT")
if match:
    print(match.group(0))

ls = re.findall(r'[1-9]\d{5}', "BIT 100081 YUS100082")
print(ls)

ls = re.split(r'[1-9]\d{5}', "BIT 100081 YUS100082")
print(ls)  # ['BIT ', ' YUS', '']

ls = re.split(r'[1-9]\d{5}', "BIT 100081 YUS100082", maxsplit=1)
print(ls)  # ['BIT ', ' YUS100082']

for m in re.finditer(r'[1-9]\d{5}', "BIT 100081 YUS100082"):
    if m:
        print(m.group(0))

str = re.sub(r'[1-9]\d{5}', ":zipcode", "BIT100081 YUS100082")
print(str)


match = re.search(r"PY.*N","PYANBNCNDN")
print(match.group(0)) #PYANBNCNDN