import turtle

def setup_game():
    # Create Ball
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 5 
    ball.dy = 4

    # Create Paddle 1
    paddle1 = turtle.Turtle()
    paddle1.shape("square")
    paddle1.color("red")
    paddle1.shapesize(stretch_wid=4, stretch_len=1)
    paddle1.penup()
    paddle1.goto(-380, 0)
    paddle1.dy = 0

    # Create Paddle 2
    paddle2 = turtle.Turtle()
    paddle2.shape("square")
    paddle2.color("blue")
    paddle2.shapesize(stretch_wid=4, stretch_len=1)
    paddle2.penup()
    paddle2.goto(370, 0)
    paddle2.dy = 0

    # Functions to move Paddles
    def paddle1_up():
        y = paddle1.ycor()
        y += 20
        paddle1.sety(y)

    def paddle1_down():
        y = paddle1.ycor()
        y -= 20
        paddle1.sety(y)

    def paddle2_up():
        y = paddle2.ycor()
        y += 20
        paddle2.sety(y)

    def paddle2_down():
        y = paddle2.ycor()
        y -= 20
        paddle2.sety(y)

    # Set up keyboard bindings
    turtle.listen()
    turtle.onkeypress(paddle1_up, "w")
    turtle.onkeypress(paddle1_down, "s")
    turtle.onkeypress(paddle2_up, "Up")
    turtle.onkeypress(paddle2_down, "Down")

    return ball, paddle1, paddle2

def main():
    # Game Screen
    turtle.setup(800, 600)
    turtle.bgcolor("black")

    # Score variables
    score1 = 0
    score2 = 0
    score_limit = 5  # Set the score limit for winning

    # Score display
    score_display = turtle.Turtle()
    score_display.color("white")
    score_display.penup()
    score_display.hideturtle()
    score_display.goto(0, 260)
    score_display.write("Player 1: 0   Player 2: 0", align="center", font=("Arial", 24, "normal"))

    ball, paddle1, paddle2 = setup_game()

    # Game loop
    while True:
        # Move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Ball collisions with top and bottom walls
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.dy *= -1

        # Paddle and ball collisions
        if (360 > ball.xcor() > 350) and (paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1
        elif (-360 < ball.xcor() < -350) and (paddle1.ycor() + 50 > ball.ycor() > paddle1.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1

        # If the ball goes past a paddle without making contact, recenter the ball, and the opposing player scores a point
        if ball.xcor() > 390:
            ball.goto(0, 0)
            score1 += 1
            score_display.clear()
            score_display.write("Player 1: {}   Player 2: {}".format(score1, score2), align="center",
                                font=("Arial", 24, "normal"))
        elif ball.xcor() < -390:
            ball.goto(0, 0)
            score2 += 1
            score_display.clear()
            score_display.write("Player 1: {}   Player 2: {}".format(score1, score2), align="center",
                                font=("Arial", 24, "normal"))

        # Check for a winner
        if score1 == score_limit or score2 == score_limit:
            winner = "Player 1" if score1 == score_limit else "Player 2"
            score_display.clear()
            score_display.write("{} wins! Game Over! Press 'x' for a new game.".format(winner),
                                align="center", font=("Arial", 24, "normal"))
            turtle.update()
            turtle.listen()
            turtle.onkeypress(restart_game, "x")
            turtle.mainloop()

        # Update screen
        turtle.update()

def restart_game():
    turtle.clearscreen()
    main()

if __name__ == "__main__":
    main()