import items, enemies, actions, world, time,game
import Background_music
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def available_inventories(self, the_player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        # Returns all the possible actions which can be taken by the player
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
 
    def available_actions(self, the_player):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
 
        return moves

    def is_this_the_room(self, player):
        raise NotImplementedError()


class SpeedyCafe(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
            return """
            Welcome to level 2!
            Your Next case: 
            A famous businessman died of cancer in the hospital. His last words before dying were "You have to go to the Corner". 
            No one understood the context behind his last words but when police investigated his background, they got to know that he is 
            hiding a very precious treasure which was stolen 5 years ago. 
            "YOU HAVE TO GO TO THE CORNER"
            What do you think? where is the treasure?   

            You will be starting from Speedy Cafe. One of Sherlock Holme's favorite spot
        """
        
    def is_this_the_room(self, player):
        pass

    def modify_player(self, player):
        pass

    def available_inventories(self, the_player):
        pass

class BartholomewHospital(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
            return """
            Welcome to level 3!
            Your Next case and final case: 
            Welcome to the last level Genius!! 
            Prof Moriarty is spreading a lot of violence around the city. Innocent people are losing their lives. You need to find Moriarty and kill him. 

            Hint: Prof Moriarty is very strong. make sure to carry along powerful weapons.  

            You will be starting from BartholomewHospital.
        """
        
    def is_this_the_room(self, player):
        pass

    def modify_player(self, player):
        pass

    def available_inventories(self, the_player):
        pass

class BakerStreet21(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
            return """
                     _               _            _    _           _                     
    | |             | |          | |  | |         | |                    
 ___| |__   ___ _ __| | ___   ___| | _| |__   ___ | |_ __ ___   ___  ___ 
/ __| '_ \ / _ \ '__| |/ _ \ / __| |/ / '_ \ / _ \| | '_ ` _ \ / _ \/ __|
\__ \ | | |  __/ |  | | (_) | (__|   <| | | | (_) | | | | | | |  __/\__ \\
|___/_| |_|\___|_|  |_|\___/ \___|_|\_\_| |_|\___/|_|_| |_| |_|\___||___/


                  ,N.
                  _/__ \   If you eliminate all other possibilities
                   -/o\_\  the one that remains, however unlikely,
                 __\_-./   is the right answer.
                / / V \`U-.
    ())        /, > o <    \  "Elementary my dear Watson"
    <\.,.-._.-" [-\ o /__..-'  
    |/_  ) ) _.-"| \o/  |  \ o!0
       `'-'-" 
                  


Hey Sherlock!! Can you find me? 
            Rules -
            1. You will get one clue each level. You have to figure out in which location the murderer is.
            2. Once you get the location of the murderer, you cannot go to the room directly, you have to go through different paths to reach there. 
                Note: Only one path is possible to reach that location.
            2. You will find different enemies in different location sent by Prof Moriarty. So be equipped with weapons.
            3. You have to find weapons in different rooms. (You can get either guns, weapons or dagger) 
            4. Your best friend Dr. Watson, Housekeeper Mrs Hudson and your Girlfriend Irene Adler can help you with some imortant clues to find the exact room
            5. You have to go to different rooms and as per the clue decide that if the murderer is in the room or no. You will get 2 chances to guess.
            6. You will have 100hp, as per the encounters with different enemies your Hp will decrease. if it becomes 0 you die. 
            

    Your first case is:
    London is in great danger!!! The police is looking for a psycho murderer named "Darth Vader" who after every murder leaves a binary note. 
    It seems like he is giving some information regarding the next murder.
    Catch him before he commits another murder. 
    The binary code is : 
    10100|1000|101|1|10100|10010|101|   | 

    Your journey starts from "21 Baker Street"   
        """
        
    def is_this_the_room(self, player):
        pass

    def modify_player(self, player):
        pass

    def available_inventories(self, the_player):
        pass
        
        
class LootRoom(MapTile): 
    def add_loot(self, player):
        player.inventory.append(self.item)
 
    def modify_player(self, player):
        self.add_loot(player)

class LondonSuperStore(LootRoom):
    def intro_text(self):
        return """
        Welcome to LondonSuperStore. You see your Housekeeper Mrs. Hudson is shopping. 
        "Do you need any help from her?"
        """
    def is_this_the_room(self, player):
        the_truth = input(" Press y if you think she can help you with some inventories or n if not: ")
        if the_truth == 'y':
            for i in player.inventory:
                if i.name == "Dagger":
                    i.value = i.value + 1
                    print("\n Mrs Hudson gave you a dagger. She thinks you need it more. The available Dagger is: ", i.value)
            
        else:
            print(" You don't need any help from Mrs. Hudson")

    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass  

class WatsonHouse(LootRoom):
    def intro_text(self):
        return """
        You are at your best companion's house - Dr. Watson
        You see a Pistol hidden under the dinning table
        """
    def is_this_the_room(self, player):
        the_truth = input(" Press y if you want to steal the weapon or n if not: ")
        if the_truth == 'y':
            for i in player.inventory:
                if i.name == "Modified_Pistol":
                    i.value = i.value + 5
                    print("\n You stole Watson's modified pistol ", i.value)
            
        else:
            print(" You don't need any help from Mrs. Hudson")

    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass  

class InventoryRoom(LootRoom):
    def intro_text(self):
        return """
        Welcome to the inventory room, You can collect different weapons from here.
        You see Revolver Ammos. Pick it up
        """
    def is_this_the_room(self, player):
        the_truth = input(" Press y if you want to pick the ammos or n if not: ")
        if the_truth == 'y':
            for i in player.inventory:
                if i.name == "Gun_Revolver":
                    i.value = i.value + 5
                    print("\n You have picked up the ammos. The available bullets in your Revolver is: ", i.value)
            
        else:
            print(" No Revolver ammos taken from the inventory room")
        

    def modify_player(self, player):
        pass

    def available_inventories(self, the_player):
        pass

class SecretRoom(LootRoom):
    def intro_text(self):
        return """
        Welcome to the Secret room, You can collect different weapons from here.
        You see a very power weapon. A Shot Gun. It's very powerful  
        """
    def is_this_the_room(self, player):
        the_truth = input(" Press y if you want to pick the Shot gun or n if not: ")
        if the_truth == 'y':
            for i in player.inventory:
                if i.name == "Gun_Shotgun":
                    i.value = i.value + 1
                    print("\n You have picked up Shot Gun. Number of bullets is: ", i.value)
            
        else:
            print(" You did not picked up Shot Gun from the secret room")
        

    def modify_player(self, player):
        pass

    def available_inventories(self, the_player):
        pass

class MarketPlace(MapTile):
    def intro_text(self):
        print('You have entered the market place. The market place is all time crowded \n') 
        print('Just be cautious and be prepared, someone might attack you \n')
        
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass

    def available_inventories(self, the_player):
        pass   

class WhiteCityBusStation(MapTile):
    def intro_text(self):
        return """
        You can now see White City Bus Station on your left. 

        Are you sure you are at the right direction?
        """
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer is or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass

    def available_inventories(self, the_player):
        pass   

class HydePark(MapTile):
    def intro_text(self):        
        print('Hyde Park is here. One of the famous park in the city. \n') 
        print('Last week there was a encounter at this place. - Just for your Knowledge')
        
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """  
    def modify_player(self, player):
        pass

    def available_inventories(self, the_player):
        pass 

class TheatreRoyalDrury(MapTile):
    def intro_text(self):
        return """
        Bringing the world inside. Welcome to TheatreRoyalDrury
        "Why is the Theatre closed today?"
        """
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """  
    def modify_player(self, player):
        pass

    def available_inventories(self, the_player):
        pass



class NationalMaritimeMuseum(MapTile):
    def intro_text(self):
        return """
        You are now going to cross the National Maritime Museum.

        "The museum was established in 1934. The museum was created by the National Maritime Museum Act under a Board of Trustees, appointed by HM Treasury"
        """
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """

    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass   

class HanwellZoo(MapTile):
    def intro_text(self):
        return """
        Hanwell Zoo - Go wild in West London. Discover the Animals

        "Hanwell Zoo is popular attraction located in Brent Lodge Park Hanwell, London W7"
        """
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """   
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass

class TheBritishMuseum(MapTile):
    def intro_text(self):
        return """
        Welcome to one of the most ancient Museum - The British Museum
        """
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """   
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass

class TescoSuperStore(MapTile):
    def intro_text(self):
        return """
        Tesco Superstore
        "Wonder why its always closed? Oh the tesco brothers are having some clashes. May be because of that"  
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass

class DollisHill(MapTile):
    def intro_text(self):
        return """
        You are now going to enter Dollis Hill. 

        "There are many Black cars overtaking you. Do you find anything suspicious?"
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass  

class CrystalPalacePark(MapTile):
    def intro_text(self):
        return """
        You have reached Crystal palace park. Watch Out!!
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass  

class DenmarkHill(MapTile):
    def intro_text(self):
        return """
        Welcome to Denmark Hill!!
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass  

class ChelseaPhysicGarden(MapTile):
    def intro_text(self):
        return """
        Welcome to Chelsea Physic Garden!!
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass  

class StonyhurstUniversity(MapTile):
    def intro_text(self):
        return """
        Welcome to Stonyhurts University. Prof James Moriarty is a well known professor of this University!!
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass  

class ZenPharmacy(MapTile):
    def intro_text(self):
        return """
        Welcome to Zen Pharmacy. This medical is famous for its service and faculty
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass 

class MarketHall(MapTile):
    def intro_text(self):
        return """
        Welcome to Market Hall!!
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass 

class LondonCityAirpot(MapTile):
    def intro_text(self):
        return """
        "Welcome to London City Airpot"
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """ 
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass 

class MarbelArch(MapTile):
    def intro_text(self):
        return """
        Welcome to Marbel Arch - A place where you will find variety of unique show peices. 

        "It's a bit costly shop because here everything is hand made" 
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass

class GardenSquare(MapTile):
    def intro_text(self):
        return """
        Garden Square one of the biggest Garden in London. 

        "Recently people have started complaining about the hygiene of the place. It doesn't smell good"
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass  

class CafeCorner(MapTile):
    def intro_text(self):
        return """
        A pretty famous Cafe in the City. Welcome to Cafe Corner!!!
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass  

class TheatreSpace(MapTile):
    def intro_text(self):
        music = Background_music.Theatre_Space()
        music.play_background()
        return """
        Welcome to Theatre Space. Come and Compare your real and reel life here. A theatre that opens daily for you

        "There is something odd about this theatre. Do you feel like checking? "
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = True
            player.truth   = True
        elif the_truth == 'n':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass    

class VaticanMuseum(MapTile):
    def intro_text(self):
        # music = Background_music.Theatre_Space()
        # music.play_background()
        return """
        Vatician Museum: Immense collection amassed by the Catholic Church and the papacy throughout the centuries, 
        including several of the most renowned Roman sculptures and most important masterpieces of Renaissance art in the world.
        
        The Name of the owner of the Museum is : Dwayne Corner 
        """ 
    def is_this_the_room(self, player):
        the_truth = input('Press y if you think the current location is the answer or press n: ')
        if the_truth == 'y':
            player.victory = True
            player.truth   = True
        elif the_truth == 'n':
            player.victory = False
            player.truth   = False
        else:
            return """
            Wrong key selected
            """
    def modify_player(self, player):
        pass
    def available_inventories(self, the_player):
        pass   

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy's hp {}".format(self.enemy.hp))
            print("Enemy does {} damage.".format(self.enemy.damage))

    def available_actions(self, the_player):
        attack_option = []
        hotkey = 'a'
        name = 'none'
        if self.enemy.is_alive():
            for i in the_player.inventory:                
                if(i.value > 0):                    
                    attack_option.append(actions.Attack(enemy=self.enemy,name = i.name, hotkey = hotkey))
                    hotkey = chr(ord(hotkey) + 1)
            return attack_option
        else:
            return self.adjacent_moves()
                    

    def available_inventories(self, the_player):
        if self.enemy.is_alive():
            print("Your Possible attack ")
            for i in the_player.inventory:
                if(i.value > 0):
                    print(": ", i.name, "value: ",i.value, "damage: ",i.damage)


class LocalAttacker(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.LocalAttacker())
    
    def intro_text(self):
        music = Background_music.Local_Attacker()
        music.play_background()
        if self.enemy.is_alive():
            print('An unknown Person was following you right from the beginning. He might be a Local Attacker \n')
            time.sleep(3) # 3 seconds of dramatic pause
            return"""
            It looks like he was sent by Prof James Moriarty. Fight him. 
            """
        else:
            music.stop_background()
            return """
            You killed Jack the ripper
             """
    def is_this_the_room(self, player):
        pass

class RedEyedHound(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.RedEyedHound())
    
    def intro_text(self):
        music = Background_music.Red_Eyed_Hound()
        music.play_background()
        if self.enemy.is_alive():
            print('Watch out, A red eyed Hound is running towards you \n')
            return"""
            Fight the Hound. 
            """
        else:
            music.stop_background()
            return """
            You killed Red eyed hound
             """
    def is_this_the_room(self, player):
        pass

class ProfessionalShooter(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ProfessionalShooter())
    
    def intro_text(self):
        music = Background_music.Professional_Shooter()
        music.play_background()
        if self.enemy.is_alive():
            print('You are walking and studdenly you sense that someone is watching you \n')
            time.sleep(3) # 3 seconds of dramatic pause
            music.stop_background()
            return"""
            There is a Professional shooter hiding somewhere. His Snipper is towards you. He can directly kill you.
            """
        else:
            return """
            
             """
    def is_this_the_room(self, player):
        pass

class JackTheRipper(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.JackTheRipper())
    
    def intro_text(self):
        music = Background_music.Jack_The_Ripper()
        music.play_background()
        if self.enemy.is_alive():
            print('Jack the ripper was searching for you. He is somewhere near you \n')
            time.sleep(2) # 2 seconds of dramatic pause
            return"""
            He is coming to attack you. Fight him.
            """
        else:
            music.stop_background()
            return """
            You killed Jack the ripper
             """
    def is_this_the_room(self, player):
        pass

class ColonelSebastianMoran(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ColonelSebastianMoran())
    
    def intro_text(self):
        #music = Background_music.Jack_The_Ripper()
        #music.play_background()
        if self.enemy.is_alive():
            print("Colonel Sebastian Moran, The Right hand man of Moriarty is here to kill you \n")
            time.sleep(2) # 2 seconds of dramatic pause
            return"""
            He is coming to attack you. Fight him.
            """
        else:
            #music.stop_background()
            return """
            You killed Colonel Sebastian Moran
             """
    def is_this_the_room(self, player):
        pass

class ProfessionalFighter(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ProfessionalFighter())
    
    def intro_text(self):
        #music = Background_music.Jack_The_Ripper()
        #music.play_background()
        if self.enemy.is_alive():
            print("A professional fighter is approaching you. It seems like he is a martial artist \n")
            return"""
            Fight him.
            """
        else:
            #music.stop_background()
            return """
            You killed the professional fighter
             """
    def is_this_the_room(self, player):
        pass

class DennisNilsen(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.DennisNilsen())
    
    def intro_text(self):
        #music = Background_music.Jack_The_Ripper()
        #music.play_background()
        if self.enemy.is_alive():
            print("Denis Nilsen - a serial killer who escaped from the prison. \n")
            return"""
            Fight him.
            """
        else:
            #music.stop_background()
            return """
            You killed the professional fighter
             """
    def is_this_the_room(self, player):
        pass

class JamesMoriarty(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.JamesMoriarty())
    
    def intro_text(self):
        #music = Background_music.Jack_The_Ripper()
        #music.play_background()
        if self.enemy.is_alive():
            print("You finally reached ReichenbachFall and you meet Prof James Moriarty. A Consulting criminal mastermind who does not commit crimes himself, but instead uses his intelligence and network of resources to provide criminals with strategies for their crimes \n")
            time.sleep(5) # 2 seconds of dramatic pause
            return"""
            Hope you have that special weapon to kill him
            """
        else:
            #music.stop_background()
            return """
            You killed Prof James Moriarty!!!! 

                      _______                     _________ _       
            |\     /|(  ___  )|\     /|      |\     /|\__   __/( (    /|
            ( \   / )| (   ) || )   ( |      | )   ( |   ) (   |  \  ( |
             \ (_) / | |   | || |   | |      | | _ | |   | |   |   \ | |
              \   /  | |   | || |   | |      | |( )| |   | |   | (\ \) |
               ) (   | |   | || |   | |      | || || |   | |   | | \   |
               | |   | (___) || (___) |      | () () |___) (___| )  \  |
               \_/   (_______)(_______)      (_______)\_______/|/    )_)
                                                        
             """
    def is_this_the_room(self, player):
        pass

        