import vlc
class Background_music:
    def __init__(self, background):
        self.background = background

    def play_background(self):
        self.background.play()

    def stop_background(self):
        self.background.stop()
        
class London_super_store(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\London_super_store.mp3"))

class Inventory_Room(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Inventory_Room.mp3"))

class MarketPlace(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\MarketPlace.mp3"))

class White_City_Bus_Station(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\White_City_Bus_Station.mp3"))

class Hyde_Park(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Hyde_Park.mp3"))

class Theatre_Royal_Drury(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Theatre_Royal_Drury.mp3"))

class National_Maritime_Museum(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\National_Maritime_Museum.mp3"))

class Hanwell_Zoo(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Hanwell_Zoo.mp3"))

class Tesco_Super_Store(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Tesco_Super_Store.mp3"))

class Dollis_Hill(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Dollis_Hill.mp3"))

class Crystal_Palace_Park(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Crystal_Palace_Park.mp3"))

class London_City_Airport(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\London_City_Airport.mp3"))

class Marbel_Arch(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Marbel_Arch.mp3"))

class Garden_Square(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Garden_Square.mp3"))

class Theatre_Space(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Theatre_Space.mp3"))

class Local_Attacker(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Local_Attacker.mp3"))

class Red_Eyed_Hound(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Red_Eyed_Hound.mp3"))

class Professional_Shooter(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Professional_Shooter.mp3"))

class Jack_The_Ripper(Background_music):
    def __init__(self):
        super().__init__(background = vlc.MediaPlayer(r"D:\University_Info\HOF\Semester 1\Advanced Programming\SherlockHolmes\Jack_The_Ripper.mp3"))

# obj = London_super_store()
# obj.play_background()
# time.sleep(10)
# obj.stop_background()