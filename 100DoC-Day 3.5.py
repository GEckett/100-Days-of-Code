# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1LC = name1.lower()
name2LC = name2.lower()
T = name1LC.count("t") + name2LC.count("t")
R = name1LC.count("r") + name2LC.count("r")
U = name1LC.count("u") + name2LC.count("u")
E = name1LC.count("e") + name2LC.count("e")
L = name1LC.count("l") + name2LC.count("l")
O = name1LC.count("o") + name2LC.count("o")
V = name1LC.count("v") + name2LC.count("v")
E = name1LC.count("e") + name2LC.count("e")
True_Total = T + R + U + E
Love_Total = L + O + V + E
Love_Score = int(f"{True_Total}{Love_Total}")
if Love_Score < 10 or Love_Score > 90:
    print(f"Your score is {Love_Score}, you go together like coke and mentos.")
elif Love_Score >= 40 and Love_Score <= 50:
    print(f"Your score is {Love_Score},you are alright together.")
else:
    print(f"Your score is {Love_Score}.")