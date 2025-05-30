def ask_question(question):
    answer = input(question + " (yes/no): ").strip().lower()
    while answer not in ["yes", "no"]:
        print("Invalid answer. Please respond with 'yes' or 'no'.")
        answer = input(question + " (yes/no): ").strip().lower()
    return answer == "yes"

def identify_animal():
    print("=== Animal Identification ===")

    if ask_question("Does the animal have feathers?"):
        if ask_question("Can it fly?"):
            print(">> It's probably a bird that can fly (like a dove or a sparrow).")
        else:
            print(">> It's probably a flightless bird (like an ostrich or a penguin).")
    else:
        if ask_question("Does the animal live in water?"):
            if ask_question("Does it have fins?"):
                print(">> It's probably a fish.")
            else:
                print(">> It's probably an amphibian (like a frog).")
        else:
            if ask_question("Does it have four legs?"):
                if ask_question("Is it a domestic animal?"):
                    print(">> It's probably a dog or a cat.")
                else:
                    print(">> It's probably a wild animal (like a tiger or a deer).")
            else:
                print(">> It might be a snake or an insect.")

# Run the program
identify_animal()
