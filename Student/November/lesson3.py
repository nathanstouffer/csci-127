import pandas as pd
import matplotlib.pyplot as plt

failed_banks = pd.read_csv('banklist.csv')

failed_banks["Closing Year"] = 0

for i in range(len(failed_banks)):
    year = failed_banks.ix[i, "Closing Date"]
    year = int(year[-2:]) + 2000
    failed_banks.ix[i, "Closing Year"] = year

plt.figure("Bank Information")

plt.subplot(121)
plt.xlabel("Year")
plt.ylabel("Failures")
plt.title("FDIC Failed Banks")

failed_banks["Closing Year"].value_counts().plot(kind="bar", color="red")

plt.subplot(122)
plt.xlabel("Year")
plt.ylabel("Failures")
plt.title("FDIC Failed Banks")

failed_banks["Closing Year"].value_counts(sort=False).plot("bar", color="violet")

plt.show()

