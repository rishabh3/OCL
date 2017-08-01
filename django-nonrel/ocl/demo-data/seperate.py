from ast import literal_eval as leval

l =[]
with open('ciel_20160328_mappings_2k.json','r') as mapping:
    data = mapping.read()
count = 0
c = ""
for line in data:
	if(line != '}'):
		c+=line
	else:
		c+=line
		l.append(c)
		c = ""
x = l[0]
print(type(x))
print(x)
res = leval(x)
print(type(res))

