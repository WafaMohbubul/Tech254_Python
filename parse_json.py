
import json

#Making json more understandable in Python
#.loads() - turn into a python dictionary from json string
#open() - opens file
#read() - reads the content in the file
parsed_json = json.loads(open('example_json.json').read())
value = parsed_json["name"]
print(value)

for name, test in parsed_json.items():
    print(name, test)
