import random
given = []

while(len(given) != 6):
    num = random.randint(1, 6)
    if num not in given:
        given.append(num)
j = 1
for i in given:
    print("Team: " + str(j) + " - Question: " + str(i))
    j = j + 1

print()
input("Press enter to exit ;)")
