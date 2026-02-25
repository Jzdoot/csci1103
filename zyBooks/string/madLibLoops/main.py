while True:
    stringIn = input()
    word = stringIn.split()[0]
    if word == "quit":
        break
    num = stringIn.split()[1] 
    print(f"Eating {num} {word} a day keeps you happy and healthy.")
