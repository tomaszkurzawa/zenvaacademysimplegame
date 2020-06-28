#subclasses, superclasses and inheritance
class GameCharacter:

    speed = 5 

    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount




class PlayerCharacter(GameCharacter):
    speed = 10
    def __init__(self, name,  x_pos, y_pos):
        super().__init__(name, 100, 100, x_pos, y_pos)

    def move(self, by_y_amount):
        self.y_pos += by_y_amount
        


        
player_character = PlayerCharacter('P_character',500, 500)
player_character.move(100)
print(player_character.x_pos)
print(player_character.y_pos)
