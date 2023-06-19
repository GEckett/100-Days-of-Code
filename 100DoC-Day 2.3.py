# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Days_90 = 365*90
Weeks_90 = 52*90
Months_90 = 12*90
Days_to_date = int(age)*365
Weeks_to_date = int(age)*52
Months_to_date = int(age)*12
print(f"You have {round(Days_90 - Days_to_date)} days, {round(Weeks_90 - Weeks_to_date)} weeks, and {round(Months_90 - Months_to_date)} months left.")