import json



f = open('student_data.json')

data = json.load(f)
#print(data)

for i in data:
	if (i["Gender"]=="0" and i["Name"]!="Unknown"):
		print (i["Name"].split()[0])


f.close()
