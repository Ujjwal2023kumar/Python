import json
Student_data = {"Name": "Ujjwal", "age": 20, "marks": "90",}

# convert dictionary into json string
data = json.dumps(Student_data)
print(data)
print(type(data))

# convert json string into dictionary
data = json.loads(data)
print(data["age"])