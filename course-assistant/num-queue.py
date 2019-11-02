# -----------------------------------------------------
# CSCI 127, Lab 10                                    |
# November 5, 2019                                    |
# Your Name                                           |
# -----------------------------------------------------

# class that implements the Queue data structure
class Queue():

    # constructor to take in the name of the Queue
    def __init__(self, name):
        self.name = name
        self.queue = []

    # method to add a number to the end of the queue
    def enqueue(self, number):
        self.queue.append(number)

    # method to add a number to the end of the queue
    def __iadd__(self, number):
        self.queue.append(number)
        return self

    # method to pop from the beginning of the queue
    def dequeue(self):
        return self.queue.pop()

    # method to tell if the queue is empty
    def is_empty(self):
        length = len(self.queue)
        if (length == 0 ):
            return True
        else:
            return False

    # method to return a string representation of the queue
    def __str__(self):
        output = "Contents: "
        # iterate through elements
        for element in self.queue:
            output += str(element) + " "
        return output

# -----------------------------------------------------

def main():
    numbers = Queue("Numbers")

    print("Enqueue 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.enqueue(number)
        print(numbers)

    print("\nDequeue one item")
    print("----------------")
    numbers.dequeue()
    print(numbers)

    print("\nDeque all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item dequeued:", numbers.dequeue())
        print(numbers)

    # Enqueue 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.enqueue(number)
    
    # Enqueue 15
    numbers += 15

    print("\n10, 11, 12, 13, 14, 15 enqueued")
    print("-------------------------------")
    print(numbers)

# -----------------------------------------------------

main()
