# Created by Brandon Christoffer for CS 1.1

print("Linkin Park Quiz made by Brandon Christoffer.\n")
print("This quiz will contain 10 questions. Don't use any outside sources!\n")

score = 0

def question1():
    print("Which of these was Linkin Park's first studio album?")
    print("A) Living Things\nB) Hybrid Theory\nC) A Thousand Suns\nD) Meteora\n")

    selection = input("Answer: ")
    if selection.upper() != "B":
        print("Sorry, that was incorrect! The correct answer is B!\n")
        return 0
    else:
        print("That's correct!\n")
        return 1

def question2():
    print("True or False: Hybrid Theory debuted late 2000.\n")

    selection = input("True/False: ")
    if selection.upper() != "TRUE":
        print("Sorry, that was incorrect! The correct answer is True!\n")
        return 0
    else:
        print("That's correct!\n")
        return 1

def question3():
    print("How many band members does Linkin Park currently have?\n")

    selection = input("Number: ")
    if int(selection) != 5:
        print("Sorry, that was incorrect! The correct answer is 5!\n")
        return 0
    else:
        print("That's correct!\n")
        return 1

def question4():
    print("True or False: 'In The End' is Linkin Park's most known and highest performing song.\n")

    selection = input("True/False: ")
    if selection.upper() != "TRUE":
        print("Sorry, that was incorrect! The correct answer is True!\n")
        return 0
    else:
        print("That's correct!\n")
        return 1

def question5():
    print("Who was the lead singer of Linkin Park?")
    print("A) Mike Shinoda\nB) Brad Delson\nC) Billie Joe Armstrong\nD) Chester Bennington\n")

    selection = input("Answer: ")
    if selection.upper() != "D":
        print("Sorry, that was incorrect! The correct answer is D!\n")
        return 0
    else:
        print("That's correct!\n")
        return 1

def question6():
    print("Who was the lead singer before Chester Bennington?")
    print("A) Mike Shinoda\nB) Mark Wakefield\nC) Joe Hahn\nD) Billie Joe Armstrong\n")

    selection = input("Answer: ")
    if selection.upper() != "B":
        print("Sorry, that was incorrect! The correct answer is B!\n")
        return 0
    else:
        print("That's correct!\n")
        return 1

def question7():
    print("True or False: Chester Bennington is still alive.\n")

    selection = input("True/False: ")
    if selection.upper() != "FALSE":
        print("Sorry, that was incorrect! The correct answer is False!\n")
        return 0
    else:
        print("That's correct!\n")
        return 1

def question8():
    print("How many studio albums has Linkin Park released?\n")

    selection = input("Number: ")
    if int(selection) != 7:
        print("Sorry, that was incorrect! The correct answer is 7!\n")
        return 0
    else:
        print("That's correct!\n")
        return 1

def question9():
    print("Before Linkin Park was formed, they changed their band name twice. What was their original name?")
    print("A) Dead by Sunrise\nB) Fort Minor\nC) Xero\nD) Hybrid Theory\n")

    selection = input("Answer: ")
    if selection.upper() != "C":
        print("Sorry, that was incorrect! The correct answer is C!\n")
        return 0
    else:
        print("That's correct!\n")
        return 1

def question10():
    print("True or False: Linkin Park created a collaborative album with Jay-Z called 'Collision Course'\n")

    selection = input("True/False: ")
    if selection.upper() != "TRUE":
        print("Sorry, that was incorrect! The correct answer is True!\n")
        return 0
    else:
        print("That's correct!\n")
        return 1

def quiz():
    """This function starts the quiz"""

    global score

    questions = [question1,question2,question3,question4,question5,question6,question7,question8,question9,question10]

    for question in questions:
        if question() == 1:
            score += 1
    results()

def results():
    """This function tells the user how many questions they got right and gives a response based on the amount"""
    
    global score

    if score <= 3:
        print(f"You got {score} out of 10 questions correct. It's clear you don't know much or care about Linkin Park.")
    elif score <= 6 > 3:
        print(f"You got {score} out of 10 questions correct. You know quite a bit about Linkin Park, nice.")
    elif score <= 9 > 6:
        print(f"You got {score} out of 10 questions correct. You must be a fan of Linkin Park. That's great!")
    elif score == 10:
        print(f"You got {score} out of 10 questions correct. You must be a superfan! We should be friends.")
    else:
        print("Huh? You somehow broke the program... that's weird.")

quiz()