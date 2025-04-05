from queue import Queue
from random import randint

q = Queue()


def generate_request():
    request = randint(1, 100)
    q.put(request)
    print(f"Added request: {request}\n")


def process_request():
    if not q.empty():
        request = q.get()
        print(f"Processing request: {request}\n")
    else:
        print("The queue is empty\n")


while True:
    action = input("Enter 'g' to generate, 'p' to process, 'q' to quit: \n").lower()

    match action:
        case "g":
            generate_request()
        case "p":
            process_request()
        case "q":
            print("Exiting...")
            break
        case _:
            print("Invalid input. Please enter 'g', 'p' or 'q'.\n")
