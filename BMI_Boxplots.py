"""
Generating Grouped Box plots in Seaborn
Created on Tue Nov 29 04:28:27 2016

"""

import seaborn as sns

import pandas as pd

df = pd.read_csv(r"P:\Coursera\BMI\20161129_testWrite3_mostRecent_trim_grouped.csv")

df= df[(df.Sex != 'Mixed')]
columnnames = list(df.columns.values)

print columnnames
#print df
#
## Draw a nested boxplot to show bills by day and sex
sns.boxplot(x="Continent", y="MeanBMI_BothSexes",hue="Sex", data=df, palette="PRGn")
sns.despine(offset=10, trim=True)
