import random

def main():
    if len(numbers_list) == 100:
        print(average(numbers_list))
    else:
        numbers_list.append(random.randint(1, 1000))
        main()
        

def average(p_numbers_list):
    numbers_list_sum = 0

    for i in range(len(p_numbers_list)):
        numbers_list_sum += p_numbers_list[i]

    return str(numbers_list_sum/len(p_numbers_list))
    
numbers_list = []
main()
