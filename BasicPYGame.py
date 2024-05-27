import os
import random
import math

# Clear the screen (optional)
os.system('cls' if os.name == 'nt' else 'clear')

print('Secret Weapon')
print('')

while True:
    d = int(input('Enter the difficulty level (must be greater than 4): '))
    if d <= 4:
        break
    else:
        print("Difficulty level must be greater than 4. Try again.")

x = random.randint(1, d)
y = random.randint(1, d)

for g in range(1, d+5):
    x1 = int(input('Guess for x: '))
    y1 = int(input('Guess for y: '))

    z = math.sqrt((x-x1)**2 + (y-y1)**2)

    if z == 0:
        print("You destroyed it in", g, "tries!")
        exit()
    elif z <= 3:
        print('Close!')
    else:
        print("Not close.")

print("You lost.")

