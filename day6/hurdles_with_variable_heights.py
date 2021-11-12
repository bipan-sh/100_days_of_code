def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right() is True:
        if wall_in_front() is True:
            turn_left()
        else :
            move()
        
    while right_is_clear():
        turn_right()
        move()
        turn_right()
        while wall_in_front() is not True:
            move()

while at_goal() != True:
    if wall_in_front():
        jump()
   
    elif front_is_clear():
        move()