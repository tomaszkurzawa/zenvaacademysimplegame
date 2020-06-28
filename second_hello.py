
size = (100, 200)
width = size[0] #witdh = 100
height = size[1] #height = 200
new_size = size + (300,)
#del new_size - new_size no longer exist
len(size) #2
max(size)#200
min(size)#100
does_contain = 100 in size

movement = [5, -2, -3, 4, -1]
first_movement = movement[0] #first_movement = 5
movement[0] = 7 #movement = [7, -2, -3, 4, -1]
movement.append(-5) #movement = [7, -2, -3, 4, -1, -5]
movement.remove(-3) #movement = [7, -2, 4, -1, -5]



print(does_contain)
