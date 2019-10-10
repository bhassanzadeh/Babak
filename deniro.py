import csv
import json

data = {}

with open("deniro.csv") as infile:
    rdr = csv.reader(infile)
    for row in rdr:
        if len(row) == 3: # because there is an empty list we want to avoid
            if row[0] == 'Year': # because we want to skip the headline
                continue
            row[2] = row[2].replace('"', '') # because names have "", we remove them
            data[row[2]] = {"score": int(row[1]), 'year': row[0]}

with open("deniro_json.txt","w") as outfile:
    json.dump(data, outfile, indent=4)