#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random	 
#Write the rest of your code below this line 👇
Coin_Flip = random.randint(1,2)

if Coin_Flip == 1:
    print("Heads")
else:
    print("Tails")