#Exercise 1. Import pandas under the name pd.
import pandas as pd
import numpy as np
print()

# Exercise 2. Print the version of pandas that has been imported.
print(pd.__version__)
print()

# Exercise 3. Print out all the version information of the libraries that are required by the pandas library.
pd.show_versions()
print()

# Exercise 4. Create a DataFrame df from this dictionary data which has the index labels.
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)
print(df)
print()

# Exercise 5. Display a summary of the basic information about this DataFrame and its data.
print(df.describe(include= 'all'))
print()

# Exercise 6. Return the first 3 rows of the DataFrame df.
first3 = df.iloc[0:3]
print(first3)

print()

# Exercise 7. Select just the 'animal' and 'age' columns from the DataFrame df.
animal_age = df[['animal', 'age']]
print(animal_age)
print()

# Exercise 8. Select the data in rows [3, 4, 8] and in columns ['animal', 'age']
pet_selection = df.loc[df.index[[3,4,8]], ['animal', 'age']]
print(pet_selection)

print()

# Exercise 9. Select only the rows where the number of visits is greater than 2.
visits_over2 = df[df['visits']>2]
print(visits_over2)

print()

# Exercise 10. Select the rows where the age is missing, i.e. is NaN.
missing_age = df[df.age.isna()]
print(missing_age)

print()

# Exercise 11. Select the rows where the animal is a cat and the age is less than 3.
cat_older3 = df[(df.animal == 'cat') & (df.age < 3)]
print(cat_older3)

print()

# Exercise 12. Select the rows the age is between 2 and 4 (inclusive)
age_2_to_4 = df[(df.age >=2) & (df.age <=4)]
print(age_2_to_4)

print()

# Exercise 13. Change the age in row 'f' to 1.5
df.at['f','age'] = 1.5
print(df)

print()

# Exercise 14. Calculate the sum of all visits (the total number of visits).
visit_sum = df['visits'].sum()
print(visit_sum)

print()
# Exercise 15. Calculate the mean age for each different animal in df.
age_mean = df.groupby(['animal']).mean()
print(age_mean)

print()
# Exercise 16. Append a new row 'k' to df with your choice of values for each column.
# Then delete that row to return the original DataFrame.
new_row = {'animal': 'tiger', 'age': 6.2, 'visits': 5.0, 'priority': 'no'}
df = df.append(new_row, ignore_index=True)
df.drop(10,axis=0)
print(df)

print()
# Exercise 17. Count the number of each type of animal in df.
count_animals = df['animal'].value_counts()
print(count_animals)

print()
# Exercise 18. Sort df first by the values in the 'age' in decending order,
# then by the value in the 'visit' column in ascending order.
df.sort_values(['age','visits'], ascending=[False,True],inplace=True)
print(df)

print()
# Exercise 19. The 'priority' column contains the values 'yes' and 'no'.
# Replace this column with a column of boolean values: 'yes' should be True and 'no' should be False.
# swap_T_F = df['priority'] = df['priority'].map({'yes:True', 'no:False'})
df = df.replace({'priority': {'yes': True,'no': False}})
print(df)

print()
# Exercise 20. In the 'animal' column, change the 'snake' entries to 'python'.
df['animal'] = df['animal'].replace('snake','python')
print(df)

print()
# **21.** For each animal type and each number of visits, find the mean age. In other words, each row is an animal,
# each column is a number of visits and the values are the mean ages (hint: use a pivot table).

# pivot = df.pivot_table(index=['animal'], values=['visits'], aggfunc ='sum')
# print(pivot)
pivot2 = df.pivot_table(index=['animal'], values=['visits','age'], aggfunc={'sum', 'mean'})
print(pivot2)

print()
# Exercise **22.** You have a DataFrame `df` with a column 'A' of integers. For example:
# How do you filter out rows which contain the same integer as the row immediately above?

df = pd.DataFrame({'A': [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7]})
# for i in range(len(df)):
#         if i > 0:
#                 if df.loc[i-1] == df.loc[i]:
#                         df2.


print()
# Exercise **23.** Given a DataFrame of numeric values, say
# how do you subtract the row mean from each element in the row?

df = pd.DataFrame(np.random.random(size=(5, 3))) # a 5x3 frame of float values
print(df)
print(df.mean(axis=1))
df2 = df.sub(df.mean(axis=1), axis=0)
print(df2)

print()
# Exercise **24.** Suppose you have DataFrame with 10 columns of real numbers, for example:
# Which column of numbers has the smallest sum? (Find that column's label.)

df = pd.DataFrame(np.random.random(size=(5, 10)), columns=list('abcdefghij'))
print(df.sum(axis = 0))
print("Column name:",list(dict(df.sum(axis = 0)).keys())[list(dict(df.sum(axis = 0)).values()).index
(min(df.sum(axis = 0)))],",","Low Sum value:",min(df.sum(axis = 0)))

print()
# Exercise **25.** How do you count how many unique rows a DataFrame has (i.e. ignore all rows that are duplicates)?

print()
# Exercise

print()
# Exercise

print()
# Exercise

print()
# Exercise

print()

