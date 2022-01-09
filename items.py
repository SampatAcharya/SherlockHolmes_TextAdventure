# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Gun_Revolver(Weapon):
    def __init__(self):
        super().__init__(name="Gun_Revolver",
                         description="Use the revolver gun to shoot your enemy",
                         value=5,
                         damage=15)

class Gun_Shotgun(Weapon):
    def __init__(self):
        super().__init__(name="Gun_Shotgun",
                         description="Use the Shot gun to shoot your enemy",
                         value=0,
                         damage=100)
 
class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         value=2,
                         damage=10)

class Bare_Hand(Weapon):
    def __init__(self):
        super().__init__(name="Bare_Hand",
                         description="You can fight with your bare hand if you don't have weapons",
                         value=1,
                         damage=5)

class Modified_Pistol(Weapon):
    def __init__(self):
        super().__init__(name="Modified_Pistol",
                         description="A modified pistol used by Dr. Watson",
                         value=0,
                         damage=30)