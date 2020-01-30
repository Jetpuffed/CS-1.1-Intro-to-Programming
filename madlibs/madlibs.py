# Parts of speech functions
def enter_noun():
    print("Enter a noun: ")
    entered_noun = str(input())
    return entered_noun

def enter_noun_plural():
    print("Enter a plural noun: ")
    entered_noun_plural = str(input())
    return entered_noun_plural 

def enter_verb():
    print("Enter a verb: ")
    entered_verb = str(input())
    return entered_verb

def enter_adjective():
    print("Enter an adjective: ")
    entered_adjective = str(input())
    return entered_adjective

def enter_ing():
    print("Enter a verb ending with -ing: ")
    entered_ing = str(input())
    return entered_ing

def enter_place():
    print("Enter a place: ")
    entered_place = str(input())
    return entered_place

# Receive parts of speech
adjective1 = enter_adjective()
place1 = enter_place()
adjective2 = enter_adjective()
adjective3 = enter_adjective()
noun_plural1 = enter_noun_plural()
noun_plural2 = enter_noun_plural()
noun1 = enter_noun()
verb1 = enter_verb()
noun2 = enter_noun()
verb2 = enter_verb()
verb3 = enter_verb()

# Story
line1 = "On the " + adjective1 + " to " + place1 + ", my\n"
line2 = adjective2 + " friend and I decided to invent a game. Since this\n"
line3 = "would be a rather " + adjective3 + " trip, it would need to be\n"
line4 = "a game with " + noun_plural1 + " and " + noun_plural2 + ". Using our\n"
line5 = noun1 + " to " + verb1 + ", we tried to get the " + noun2 + " next to us\n"
line6 = "to play too, but they just " + verb2 + "ed at us and " + verb3 + "ed away.\n"

list_of_lines = [line1, line2, line3, line4, line5, line6]

# Output story
for i in range(len(list_of_lines)):
    print(*list_of_lines)