import sys

print("Hello and welcome to our quiz show!")

Play = input("Would you like to play? (Yes/No) ").strip().lower()

while True:
     if Play == "yes":  
        print("Alright!")
        break
     elif Play == "no":
        print("Program stopping...")
        sys.exit()
     else:
         Play = input("Pls Enter Yes or No ").strip().lower()

questions = [
    {"question": "What is the full form of RAM? ", "answer": "random access memory"},
    {"question": "What is the full form of BIOS? ", "answer": "basic input output system"},
    {"question": "What is the full form of CPU? ", "answer": "central processing unit"},
    {"question": "What is the full form of USB? ", "answer": "universal serial bus"},
]

correct = 0
total_q = len(questions)

for q in questions:
    user_input = input(q["question"] + " ").strip().lower()
    if user_input == q["answer"]:
        print("Correct!")
        correct += 1
    else:
        print(f"Incorrect! The correct answer was {q['answer']}.")

success_percentage = (correct / total_q) * 100

print(f"You got {correct} correct answers out of {total_q}")

print(f"Your success rate is {success_percentage:.2f}%.")
   