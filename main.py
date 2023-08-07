import turtle
import pandas as pd
screen = turtle.Screen()
screen.title('Indian States Guessing Game')
image = 'indianStates.gif'
screen.addshape(image)
turtle.shape(image)

# get x and y in screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

states = pd.read_csv('indian_states_corr.csv')
game_is_on = True
count = 0
guessed = []
missed = []

while game_is_on:
    answer_state = screen.textinput(title=f'{count}/{len(states.State)} Guess the state', prompt="What's another state's name?").title()
    for state in states['State']:
        if answer_state == 'Exit':
            game_is_on = False
            for place in states.State:
                if place not in guessed:
                    missed.append(place)
            new_data = pd.DataFrame(missed)
            new_data.to_csv('missed_states.csv')
            break
        if answer_state == state:
            guessed.append(answer_state)
            count += 1
            tim = turtle.Turtle()
            tim.penup()
            tim.hideturtle()
            tim.goto(x=int(states.x[states['State'] == answer_state]), y=int(states.y[states['State'] == answer_state]))
            tim.write(arg=f'{state}', align='center')

    if count > 35:
        game_is_on = False

