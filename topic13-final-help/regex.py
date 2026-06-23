import re 

code = "EW12"

line = re.findall("[A-Z]+", code)

print(line[0])