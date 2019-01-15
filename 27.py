import json

data = '{"a":"1", "b":"2"}'

# Print original text
print("Original")
print(type(data), data)

# Print a JSON blob out
x = json.loads(data)
print("Json loads")
print(type(x), x)

# Load Json from a file into a string
with open('t.json', 'r') as f:
    t1 = json.load(f)
print("Json from a file into a json dict")
print(type(t1), t1)

# Get back the string
print("Return the string")
print("Json dumps")
y = json.dumps(x)
print(type(y), json.dumps(y))
