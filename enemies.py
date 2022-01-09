class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class JackTheRipper(Enemy):
    def __init__(self):
        super().__init__(name="Jack The Ripper", hp=50, damage=10)

class RedEyedHound(Enemy):
    def __init__(self):
        super().__init__(name="Red Eyed Hound", hp=30, damage=10)

class JamesMoriarty(Enemy):
    def __init__(self):
        super().__init__(name="James Moriarty", hp=100, damage=50)

class ProfessionalShooter(Enemy):
    def __init__(self):
        super().__init__(name="Professional Shooter", hp=100, damage=100)

class LocalAttacker(Enemy):
    def __init__(self):
        super().__init__(name="Local Attacker", hp=2, damage=2)

class ColonelSebastianMoran(Enemy):
    def __init__(self):
        super().__init__(name="Colonel Sebastian Moran", hp=100, damage=5)

class ProfessionalFighter(Enemy):
    def __init__(self):
        super().__init__(name="Professional Fighter", hp=50, damage=10)

class DennisNilsen(Enemy):
    def __init__(self):
        super().__init__(name="Dennis Nilsen", hp=40, damage=15)


