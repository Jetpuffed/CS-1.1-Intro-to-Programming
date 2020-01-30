import random

poem_open = open("poem.txt","r")
poem = poem_open.read()

#TODO: Get poem string into list of lines.
lines_list = poem.split("\n")

def selection():
    '''This function allows you to select how you want the poem arranged.'''
    print("Select how you want the poem arranged:")
    print("(1) Normal\n(2) Backwards\n(3) Random\n(4) Reverse")

    while True:
        selection = input("Number: ")
        if selection == "1":
            print(poem)
            break
        elif selection == "2":
            lines_printed_backwards()
            break
        elif selection == "3":
            lines_printed_random()
            break
        elif selection == "4":
            lines_printed_reverse()
            break
        else:
            print("Invalid selection. Please try again.")

def lines_printed_backwards():
    '''This function takes in a list of strings containing the lines of your poem as arguments and will print the poem lines out in reverse with the line numbers reversed.'''
    #TODO: Reverse the list
    lines_list.reverse()
    #TODO: Use loop to print out items in list
    for i in range(len(lines_list)):
        print(lines_list[i])

def lines_printed_random():
    '''Randomly select lines from a list of strings and print them out in random order.'''
    random_lines_list = random.sample(lines_list, len(lines_list))

    for i in range(len(lines_list)):
        print(random_lines_list[i])

def lines_printed_reverse():
    '''Reverses all the words in the poem, so it's truly backwards.'''
    for i in range(len(lines_list)):
        print(lines_list[i][::-1])

selection()