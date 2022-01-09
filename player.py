import random 
import items, world

class Player():
    attack_variable = "none"        
    def __init__(self):
        self.inventory = [items.Bare_Hand(), items.Gun_Revolver(), items.Dagger(), items.Gun_Shotgun(), items.Modified_Pistol()] #Inventory on startup
        self.hp = 100 # Health Points
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up
        self.truth   = True

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    # is_alive method
    def is_alive(self):
        return self.hp > 0   #Greater than zero value then you are still alive
 
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)

    def set_attack_variable(self, attack_input_variable):
        self.attack_variable = attack_input_variable.name

    def attack(self, enemy):
        weapon_selected = None
        for i in self.inventory:
            if(i.name == self.attack_variable):
                weapon_selected = i
                if(i.name == 'Bare_Hand'):
                    break
                else: 
                    i.value = i.value - 1
                    break 
        print("You use {} against {}!".format(weapon_selected.name, enemy.name))
        enemy.hp -= weapon_selected.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        # action_method is a function variable
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
    



            
