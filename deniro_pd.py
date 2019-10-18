import pandas as pd
import csv

years = []
scores = []
titles = []

with open("deniro.csv") as infile:
    rdr = csv.reader(infile)
    for row in rdr:
        if len(row) == 0:
            continue # because there is an empty list we want to avoid

        if row[0] == 'Year':  # because we want to skip the headline
            continue

        row[1] = row[1].replace(' ', '')
        row[2] = row[2].replace('"', '') # because names have "", we remove them
        row[2] = row[2].lstrip() # because titles have an extra space in the beginning

        if len(row) == 4: # for titles that have a comma
            row[3] = row[3].replace('"', '')
            row[3] = row[3].lstrip()
            row[2] = row[2] + ', ' + row[3]  # add the two parts
            row = row[:3]

        years.append(row[0])
        scores.append(row[1])
        titles.append(row[2])

# build the dataframe with the lists
df = pd.DataFrame({'Year': years, 'Score': scores, 'Title': titles})
df['Year'] = df['Year'].astype(int)
print(df)
print()
print(df[df['Title'] == 'Heat'])
print()
print(df[df['Year'] == 1992])