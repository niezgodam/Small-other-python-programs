import random
import sys
import os
from dotenv import load_dotenv
load_dotenv()


file_name = os.getenv('FILENAME')

if not file_name:
    print("FILENAME environment variable is not set.")
    sys.exit(1)

with open(file_name, "r", encoding="utf-8") as f:
    lines = f.readlines()


questions = lines[0::2]  
answers = lines[1::2]  
print("Press enter to see answer")
print()

while questions and answers:

    index = random.randint(0, len(questions)-1)
    if questions[index]:
        pytanie = questions[index]
    else:
        print("The questions are over")
        sys.exit(0)


    input(f"{pytanie.strip()}")

    answer = answers[index]
    print(answer.strip())
    print("")
    answers.pop(index)

    questions.pop(index)
