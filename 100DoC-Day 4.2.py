# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
No_of_people = len(names)
Rando_No = random.randint(0,No_of_people - 1)
Payer = names[Rando_No]
print(f"{Payer} is going to buy the meal today!")