# 🧩 Random Guessing Number Game 🧩 :-

print("\n" + "=" * 30)
print("🧩 RANDOM GUESSING NUMBER GAME 🧩 : ")
print("=" * 30)

import random 

# Step 1 : Developing Random Numbers -
target = random.randint(1,100)

# Step 2 : Loop -
while True :

# Step 3 : Performing Operations -
    user_choice =int(input("GUESS NUMBER : "))

    if (user_choice > target) :
        print("\n!! YOUR GUESS NUMBER IS HIGH !!")
    elif (user_choice < target) :
        print("\n!! YOUR GUESS NUMBER IS LOW !!")
    else :
        print("\n!! YOUR GUESS IS CORRECT !!")
        print("=" * 20)
        print("GAME OVER")
        print("="*20)
        break








