import world, time
from player import Player
game_level = 1
level_passed = False
def play():
    global game_level
    world.load_tiles(game_level)
    player = Player()
    #These lines load the starting room and display the text. room prints StartingRoom
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        if player.truth == False:
            break
        else:            
            room = world.tile_exists(player.location_x, player.location_y)
            room.is_this_the_room(player)
            room.modify_player(player)
            # Check again since the room could have changed the player's state
            if player.is_alive() and not player.victory:
                if player.truth == False:
                    break
                else:
                    # room.is_this_the_room(player)
                    print("\n")
                    print("+ Current Health in hp: ", player.hp, "\n")
                    room.available_inventories(player)
                    print("Choose an action:\n")
                    available_actions = room.available_actions(player)
                    for action in available_actions:
                        print(action)                    
                    action_input = input('Action: ')
                    print("_________________________________________________________________________________________ \n")
                    # if number == 1:
                    #     action_input = 'e'
                    #     number = number + 1
                    # else:
                    #     action_input = 'a'
                    for action in available_actions:
                        if action_input == action.hotkey:
                            player.set_attack_variable(action)
                            player.do_action(action, **action.kwargs)
                            break
    if player.is_alive():
        if player.victory == True:
            print("\n")
            print("You have successfully stopped the Psycho killer from doing another murder.\n")
            print("__________Case Closed: One Truth Prevails_____________ \n")
        else:
            print("\n")
            print("Wrong Location selected. Your deductions were wrong. Play again!!! \n")
            time.sleep(5)
    else:
        print("You got killed by your enemy!!! Play Again")
    global  level_passed
    level_passed = player.victory
    if(level_passed == True):
        game_level = game_level + 1

if __name__ == "__main__":
    while True:
        play()
        if (level_passed == True) and (game_level == 2):
            level_passed = False            
            play()
        if (level_passed == True) and  (game_level == 3):
            game_level = 3
            play()
     
    
