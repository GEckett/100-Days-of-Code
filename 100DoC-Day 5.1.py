# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
no_of_heights = n + 1
total = 0
for height in student_heights:
    total += height


Avg_Height = total / no_of_heights
print(round(Avg_Height))