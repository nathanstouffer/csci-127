import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

how_many = 1000         # number of submissions
file_name = "jbd.csv"   # file to write to and then read from

# Create Data --------------------------

names = ['HughJ', 'Ryan', 'Justin', 'Sam', 'Michael', 'Grace',
         'Courtney', 'Chris', 'Kyle', 'Tyler', 'HughO']

# np.random.seed(2017)
random_names = list(map((lambda x: names[x]),
                        np.random.randint(0, len(names), how_many)))
print("First 5 names:", random_names[:5], "\n")

scores = np.random.randint(0, 101, how_many)
print("First 5 scores:", scores[:5], "\n")

cs_data_set = list(zip(random_names,scores))
print("First 5 Zipped Names and Scores")
print("-----------------------------")
print(cs_data_set[:5])

data_frame = pd.DataFrame(data = cs_data_set, columns=['Names', 'Scores'])
print("\nFirst 5 Items in Data Frame")
print("---------------------------")
print(data_frame[:5])

data_frame.to_csv(file_name,index=False,header=True)

# Access Data --------------------------

jbd_data_frame = pd.read_csv(file_name)
print("\nFirst 5 Items in Data Frame From File")
print("-------------------------------------")
print(jbd_data_frame[:5])

print("\nData Frame Info")
print("---------------")
print(jbd_data_frame.info())

print("\nData Frame Head")
print("---------------")
print(jbd_data_frame.head())

print("\nData Frame Tail")
print("---------------")
print(jbd_data_frame.tail(3))

# Manipulate Data ----------------------

print("\nUnique Names in Data Frame")
print("--------------------------")
for name in jbd_data_frame['Names'].unique():
    print(name)

jbd_object = jbd_data_frame.groupby('Names')
print("\nDescribe Data Frame")
print("-------------------")
print(jbd_object.describe())

condensed_data_frame = jbd_object.sum()
print("\nFirst 5 Items in Condensed Data Frame After Sum")
print("-----------------------------------------------")
print(condensed_data_frame[:5])

condensed_data_frame = condensed_data_frame.sort_values(['Scores'])
print("\nFirst 5 Items in Condensed Data Frame After Sort")
print("------------------------------------------------")
print(condensed_data_frame[:5])

# Present Data -------------------------

condensed_data_frame['Scores'].plot.bar(color="turquoise")
plt.xlabel("Student")
plt.ylabel("Points Earned")
plt.title("Joy and Beauty of Data Dashboard")
plt.show()

# Clean-Up -----------------------------

os.remove(file_name)

