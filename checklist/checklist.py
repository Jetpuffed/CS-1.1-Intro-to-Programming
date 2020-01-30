checklist = []

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1

def mark_completed(index):
    update(index, "√" + checklist[index])

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index: ")

        # Remember that item_index must actually exist or our program will crash.
        read(int(item_index))

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False

    # Catch all
    else:
        print("Unknown Option")

    return True

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list, Q to quit: ")
    running = select(selection)