import random


with open("pytania_odpowiedzi.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()


pytania = lines[0::2]  
odpowiedzi = lines[1::2]  

for i in range(len(pytania)):

    index = random.randint(0, len(pytania)-1)
    pytanie = pytania[index]


    input(f"{pytanie.strip()}")

    odpowiedz = odpowiedzi[index]
    print(odpowiedz.strip())
    print("")
    odpowiedzi.pop(index)

    pytania.pop(index)