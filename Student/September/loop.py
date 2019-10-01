
print("Loop with continue\n")
for i in range(2000, 2017):
    if i % 7 == 0:
        continue
    print(i)

print("\nLoop with break\n")
for i in range(2000, 2017):
    if i % 7 == 0:
        break
    print(i)

print("\nDemonstration finished")
