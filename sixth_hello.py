#functions
x_pos = 0
e_x_pos = 4
print(x_pos)
#function to increase x_pos by 1 
def move():
    global x_pos #must retrieve the global value
    x_pos +=1 #changes the value of the global x_pos
move()    #runs the code in the move function
def move_by(amount):
    global x_pos 
    x_pos += amount

def check_for_collision():
    global x_pos
    global e_x_pos
    if x_pos == e_x_pos:
        return True
    else:
        return False
move_by(3)
did_collide = check_for_collision()
print(x_pos)
print(did_collide)
    
