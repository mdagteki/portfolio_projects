from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.level = 1
		self.update_scoreboard()

	def update_scoreboard(self):
		self.clear()
		self.goto(-370, 260)
		self.write(f"Level:{self.level}", align="left", font=FONT)

	def level_point(self):
		self.level += 1
		self.update_scoreboard()

	def game_over(self):
		self.hideturtle()
		self.penup()
		self.goto(0, 0)
		self.write("GAME OVER", align="center", font=FONT)
