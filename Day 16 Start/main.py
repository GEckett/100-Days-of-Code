#from turtle import Turtle, Screen
#timy = Turtle()
#my_screen = Screen()
#print(timy)
#timy.shape("turtle")
#timy.color("green")
#timy.forward(100)
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)