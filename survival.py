import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# read the data
df = pd.read_csv('train.csv')


# first, we find the age groups for the x axis
age_groups = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# then, we find the data for each group

survived_male_10 = df[(df['Survived'] == 1) & (df['Sex']=='male') & (df['Age'] < 10)]
survived_male_20 = df[(df['Survived'] == 1) & (df['Sex']=='male') & (df['Age'] >= 10) & (df['Age'] < 20)]
survived_male_30 = df[(df['Survived'] == 1) & (df['Sex']=='male') & (df['Age'] >= 20) & (df['Age'] < 30)]
survived_male_40 = df[(df['Survived'] == 1) & (df['Sex']=='male') & (df['Age'] >= 30) & (df['Age'] < 40)]
survived_male_50 = df[(df['Survived'] == 1) & (df['Sex']=='male') & (df['Age'] >= 40) & (df['Age'] < 50)]
survived_male_60 = df[(df['Survived'] == 1) & (df['Sex']=='male') & (df['Age'] >= 50) & (df['Age'] < 60)]
survived_male_70 = df[(df['Survived'] == 1) & (df['Sex']=='male') & (df['Age'] >= 60) & (df['Age'] < 70)]
survived_male_80 = df[(df['Survived'] == 1) & (df['Sex']=='male') & (df['Age'] >= 70) & (df['Age'] < 80)]
survived_male_90 = df[(df['Survived'] == 1) & (df['Sex']=='male') & (df['Age' ]>= 80) & (df['Age'] < 90)]
survived_male_100 = df[(df['Survived'] == 1) & (df['Sex']=='male') & (df['Age' ]>= 90) & (df['Age'] < 100)]


survived_female_10 = df[(df['Survived'] == 1) & (df['Sex']=='female') & (df['Age'] < 10)]
survived_female_20 = df[(df['Survived'] == 1) & (df['Sex']=='female') & (df['Age'] >= 10) & (df['Age'] < 20)]
survived_female_30 = df[(df['Survived'] == 1) & (df['Sex']=='female') & (df['Age'] >= 20) & (df['Age'] < 30)]
survived_female_40 = df[(df['Survived'] == 1) & (df['Sex']=='female') & (df['Age'] >= 30) & (df['Age'] < 40)]
survived_female_50 = df[(df['Survived'] == 1) & (df['Sex']=='female') & (df['Age'] >= 40) & (df['Age'] < 50)]
survived_female_60 = df[(df['Survived'] == 1) & (df['Sex']=='female') & (df['Age'] >= 50) & (df['Age'] < 60)]
survived_female_70 = df[(df['Survived'] == 1) & (df['Sex']=='female') & (df['Age'] >= 60) & (df['Age'] < 70)]
survived_female_80 = df[(df['Survived'] == 1) & (df['Sex']=='female') & (df['Age'] >= 70) & (df['Age'] < 80)]
survived_female_90 = df[(df['Survived'] == 1) & (df['Sex']=='female') & (df['Age'] >= 80) & (df['Age'] < 90)]
survived_female_100 = df[(df['Survived'] == 1) & (df['Sex']=='female') & (df['Age'] >= 90) & (df['Age'] < 100)]

# finally, we calculate the total number of survived people in each group
total_survived_male_10 = survived_male_10['Survived'].sum()
total_survived_male_20 = survived_male_20['Survived'].sum()
total_survived_male_30 = survived_male_30['Survived'].sum()
total_survived_male_40 = survived_male_40['Survived'].sum()
total_survived_male_50 = survived_male_50['Survived'].sum()
total_survived_male_60 = survived_male_60['Survived'].sum()
total_survived_male_70 = survived_male_70['Survived'].sum()
total_survived_male_80 = survived_male_80['Survived'].sum()
total_survived_male_90 = survived_male_90['Survived'].sum()
total_survived_male_100 = survived_male_100['Survived'].sum()


total_survived_female_10 = survived_female_10['Survived'].sum()
total_survived_female_20 = survived_female_20['Survived'].sum()
total_survived_female_30 = survived_female_30['Survived'].sum()
total_survived_female_40 = survived_female_40['Survived'].sum()
total_survived_female_50 = survived_female_50['Survived'].sum()
total_survived_female_60 = survived_female_60['Survived'].sum()
total_survived_female_70 = survived_female_70['Survived'].sum()
total_survived_female_80 = survived_female_80['Survived'].sum()
total_survived_female_90 = survived_female_90['Survived'].sum()
total_survived_female_100 = survived_female_100['Survived'].sum()


# plotting
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(7, 6))

width = 2

males_total_data = [total_survived_male_10, total_survived_male_20, total_survived_male_30, total_survived_male_40,
                   total_survived_male_50, total_survived_male_60, total_survived_male_70, total_survived_male_80, 
                   total_survived_male_90, total_survived_male_100]

females_total_data = [total_survived_female_10, total_survived_female_20, total_survived_female_30, total_survived_female_40,
                   total_survived_female_50, total_survived_female_60, total_survived_female_70, total_survived_female_80, 
                   total_survived_female_90, total_survived_female_100]


males = ax.bar(age_groups - width/2, males_total_data, width, label='Male')
females = ax.bar(age_groups + width/2, females_total_data, width, label='Female')


ax.set_title('Survival by Age and Gender')
ax.set_xlabel('Age')
ax.set_ylabel('Count')
ax.legend()

plt.show()