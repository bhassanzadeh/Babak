import json
import pandas as pd

with open("baby_names.txt") as infile:
    data = json.load(infile)

names_dict = data['top']
df = pd.DataFrame({'Name': list(names_dict.keys()), 'Count':list(names_dict.values())})


#Remove all names that contain the letter “v”
df = df[~df["Name"].str.contains("v")]

#Remove any instances of the following names: [“Gary”, “Aaron”, “Luke”, “Winston”, “Avery”]
df = df[df["Name"]!='Gary']
df = df[df["Name"]!='Aaron']
df = df[df["Name"]!='Luke']
df = df[df["Name"]!='Winston']
df = df[df["Name"]!='Avery']


# Remove any names with a count of “28”
df = df[df["Count"]!='28']

#Add the name “Ron” with a count of “5”
df = df.append({'Name': 'Ron', 'Count': 5}, ignore_index=True)

print(df)