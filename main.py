import turtle
from turtle import Screen, Turtle
from snake_class import Snake
from food import Food
from scoreboard import ScoreBoard
import time


# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Menu turtle for start/end messages
menu = Turtle()
menu.hideturtle()
menu.penup()
menu.color("white")


def show_start_menu():
    menu.clear()
    menu.goto(0, 60)
    menu.write("SNAKE GAME", align="center", font=("Courier", 36, "bold"))
    menu.goto(0, 0)
    menu.write("Press SPACE to Start", align="center", font=("Arial", 20, "normal"))
    menu.goto(0, -40)
    menu.write("Press ESC to Quit", align="center", font=("Arial", 14, "normal"))
    screen.update()


def show_end_menu():
    menu.clear()
    menu.goto(0, 60)
    menu.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
    menu.goto(0, 0)
    menu.write("Press SPACE to Play Again", align="center", font=("Arial", 20, "normal"))
    menu.goto(0, -40)
    menu.write("Press ESC to Quit", align="center", font=("Arial", 14, "normal"))
    screen.update()


# Objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Hide game objects until game starts
for seg in snake.segments:
    seg.hideturtle()
food.hideturtle()


# Game state
game_is_on = False


def start_game():
    global game_is_on
    if not game_is_on:
        menu.clear()
        snake.reset()
        for seg in snake.segments:
            seg.showturtle()
        food.refresh()
        food.showturtle()
        scoreboard.update_scoreboard()
        game_is_on = True
        screen.update()


def exit_game():
    screen.bye()


# Keys to use
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(start_game, "space")
screen.onkey(exit_game, "Escape")


# Show start menu
show_start_menu()

# Main loop
try:
    while True:
        screen.update()
        time.sleep(0.15)

        if not game_is_on:
            continue

        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            game_is_on = False
            show_end_menu()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()
                game_is_on = False
                show_end_menu()

except turtle.Terminator:
    pass
