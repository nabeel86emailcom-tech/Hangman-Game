import random
from wordlist import my_list
from personimage import list
from hangman_logos import logos

print(random.choice(logos))
choosed=random.choice(my_list)
new_list=["_"]*len(choosed)
print(new_list)
chances=6
gameover=False
while not gameover:
    guesslatter=input(" 🤔 Guess a latter Please:")

    for position in range(len(choosed)):
        latter=choosed[position]
        if guesslatter==choosed[position]:
            new_list[position]= latter
            print(new_list)

    if "_" not in new_list:
        print("You Won...Congratulations You Saved A Life ")
        gameover=True

    if guesslatter not in choosed:
        chances -= 1
        print(f"⚠️ You Have Only {chances} More Chances To Save A Life")
        if chances== 0:
            print("You Kill A Person 🤦‍♂️")
            gameover=True
            
print(list[chances])
print(f"Word is {choosed}")      
print(f"Your guess is {new_list}")
