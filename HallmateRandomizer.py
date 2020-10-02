import random

hallmates_name_list = []
iteration_number = 1

manual_list_input_question = ""
while manual_list_input_question == "":
    manual_list_input_question = str(input("Do you want to enter the hallmates manually? (y/n): "))
if manual_list_input_question == "y":
    manual_list_input = True
else:
    manual_list_input = False

if manual_list_input == True:
    number_of_hallmates = int(input("How many hallmates do you have?: "))
    while iteration_number <= number_of_hallmates:
        name_hallmate = str(input("What is the name of the hallmate from room " + str(iteration_number) + "?: "))
        hallmates_name_list.append(name_hallmate)
        iteration_number += 1
else: 
    hallmates_name_list = ["Quinten", "Wouter", "Puck", "Robin", "Aysa", "Thomas", "Florian", "Joke", "Lotte", "Lou", "Titia", "Alwin", "Marieke", "Juliane", "Maarten"]
    number_of_hallmates = len(hallmates_name_list)

def get_random_list(number_of_hallmates, hallmates_name_list):
    print("\nThe new random sequence of hallmates is: ")
    sequence_random = random.sample(hallmates_name_list, number_of_hallmates)
    i = 1
    room_number = 1
    for x in sequence_random:
        room_number = hallmates_name_list.index(x) + 1
        print(str(i) + ": " + x + " (Room " + str(room_number) + ")")
        i += 1

def try_again():
    try_again_question = ""
    while try_again_question == "":
        try_again_question = str(input("You want to generate a new random list of these same hallmates? (y/n): "))
    if try_again_question == "y":
        return True
    else:
        return False

get_random_list(number_of_hallmates, hallmates_name_list)
while try_again():
    get_random_list(number_of_hallmates, hallmates_name_list)

