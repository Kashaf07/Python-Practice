import sys

class QueueDemo:
    front = 0
    rear = 0
    queueData = []
    size = 0

    def __init__(self, size):
        self.size = size

    def isFull(self):
        return self.rear == self.size

    def isEmpty(self):
        return self.front == self.rear

    def enqueue(self, x):
        if self.isFull():
            print("Queue is Full")
        else:
            self.queueData.append(x)
            self.rear += 1
            print("One Element is Enqueued")
            print(self.rear)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("One Element is Dequeued:", self.queueData[self.front])
            self.front += 1
            print(self.front)

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front Element is Peeked:", self.queueData[self.front])

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            for n in range(self.front, self.rear):
                print("Element ->", self.queueData[n])

# Example usage:
queue1 = QueueDemo(5)
choice = 0
print("Welcome to the NUV\n")
print("1: Enqueue \n2: Dequeue \n3: Peek \n4: Display \n5: Exit")

while True:
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        t = input("Enter Value: ")
        queue1.enqueue(t)
    elif choice == 2:
        queue1.dequeue()
    elif choice == 3:
        queue1.peek()
    elif choice == 4:
        queue1.display()
    elif choice == 5:
        sys.exit()
    else:
        print("Invalid Data")
