import numpy as np
import math

def mean(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

def standard_deviation(numbers):
    average = mean(numbers)
    variance = 0
    for number in numbers:
        variance += (average - number) ** 2
    variance = variance / len(numbers)
    return math.sqrt(variance)

def sort(numbers):
    for i in range(len(numbers) - 1):
        smallest_index = i
        for j in range(i+1, len(numbers)):
            # if numbers[j] < numbers[smallest_index]:
            if numbers[j] > numbers[smallest_index]:
                smallest_index = j
        numbers[i], numbers[smallest_index] = numbers[smallest_index], numbers[i]

shoulder_heights = np.array([600, 470, 170, 430, 300])
print("Original Array:", shoulder_heights)
print("Mean:", mean(shoulder_heights))
print("Standard Deviation:", standard_deviation(shoulder_heights))
sort(shoulder_heights)
print("Sorted Array:", shoulder_heights)

