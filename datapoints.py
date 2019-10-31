import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))

male_df = df[df['Sex'] == 'male']
female_df = df[df['Sex'] == 'female']

# first plot
ax[0,0].scatter(male_df.Age, male_df.SibSp)
ax[0,0].set_title('Male SibSp')
ax[0,0].set_xlabel('Age')
ax[0,0].set_ylabel('Number of Siblings/Spouses')
ax[0,0].set_xlim(0, 100)

# second plot
ax[0,1].scatter(female_df.Age, female_df.SibSp)
ax[0,1].set_title('Female SibSp')
ax[0,1].set_xlabel('Age')
ax[0,1].set_ylabel('Number of Siblings/Spouses')
ax[0,1].set_xlim(0, 100)

# third plot
ax[1,0].scatter(male_df.Age, male_df.Parch)
ax[1,0].set_title('Male Parch')
ax[1,0].set_xlabel('Age')
ax[1,0].set_ylabel('Number of Parents/Children')
ax[1,0].set_xlim(0, 100)

# fourth plot
ax[1,1].scatter(female_df.Age, female_df.Parch)
ax[1,1].set_title('Female Parch')
ax[1,1].set_xlabel('Age')
ax[1,1].set_ylabel('Number of Parents/Children')
ax[1,1].set_xlim(0, 100)


plt.subplots_adjust(wspace = 0.5)
plt.subplots_adjust(hspace = 0.5)
plt.show()