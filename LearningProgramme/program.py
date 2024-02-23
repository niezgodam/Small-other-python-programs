import random


with open("pytania_odpowiedzi.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()


questions = lines[0::2]  
answers = lines[1::2]  

for i in range(len(questions)):

    index = random.randint(0, len(questions)-1)
    pytanie = questions[index]


    input(f"{pytanie.strip()}")

    odpowiedz = answers[index]
    print(odpowiedz.strip())
    print("")
    answers.pop(index)

    questions.pop(index)