import json

with open("baby_names.txt") as infile:
    data = json.load(infile)

# Remove all names that contain the letter “v”
for name in list(data['top']):
    if 'v' in name:
        del data['top'][name]

# Remove any instances of the following names: [“Gary”, “Aaron”, “Luke”, “Winston”, “Avery”]
for name in list(data['top']):
    if name in ['Gary', 'Aaron', 'Luke', 'Winston', 'Avery']:
        del data['top'][name]

# Remove any names with a count of 28.
for name in list(data['top']):
    if data['top'][name] == 28:
        del data['top'][name]

# Add the name “Ron” with a count of “5”
data['top']['Ron'] = 5

# Write the resulting dictionary in JSON format in a file called better_names.txt
# The output file should be formatted with indent=4 for easier reading
with open("better_names.txt","w") as outfile:
    json.dump(data, outfile, indent=4)
