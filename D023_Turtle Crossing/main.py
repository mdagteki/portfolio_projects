import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)


screen.listen()
screen.onkeypress(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish():
        player.reset_position()
        scoreboard.level_point()
        car_manager.speed_up()


screen.exitonclick()
