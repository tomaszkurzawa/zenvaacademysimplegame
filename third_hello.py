#tuples
size = (100, 200)
width = size[0] #witdh = 100
height = size[1] #height = 200
new_size = size + (300,)
#del new_size - new_size no longer exist
len(size) #2
max(size)#200
min(size)#100
does_contain = 100 in size
#list
movement = [5, -2, -3, 4, -1]
first_movement = movement[0] #first_movement = 5
movement[0] = 7 #movement = [7, -2, -3, 4, -1]
movement.append(-5) #movement = [7, -2, -3, 4, -1, -5]
movement.remove(-3) #movement = [7, -2, 4, -1, -5]
#dicts

starting_positions = {'p_0': 50, 'p_1':100, 'p_2':150}
starting_positions['p_0'] #50
starting_positions.keys() #['p_0', 'p_1', 'p_2']
print(starting_positions.values()) #[50, 100, 150]
