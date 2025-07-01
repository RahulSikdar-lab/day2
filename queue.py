queue = []
def enqueue(x):
    queue.append(x)
    print(f"Inserted: {x}")

def dequeue():
    if queue:
        x = queue.pop(0)
        print(f"Removed: {x}")
    else:
        print("Queue is empty")
def display():
    print("Queue:", queue)
enqueue(10)
enqueue(20)
enqueue(30)
enqueue("rahul")
print(queue)
dequeue()
print(queue)
