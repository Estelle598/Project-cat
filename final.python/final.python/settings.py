class Settings:
    """A class to store all the settings"""

    def __init__(self):
        """Initialize the game's static settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (168,100,98)

        #Ship Settings
        self.ship_limit = 3

        #Bullet settings
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3

        #Alien settings
        self.fleet_drop_speed = 10


        #How fast the game spedds up
        self.speedup_scale = 1.1

        self.background_image_path = '/home/kali/Desktop/final.python/templates/home.jpg'

        self.initialize_dynamic_settings()
    
    def get_background_image_path(self):
        """Return the path of the background image"""
        return self.background_image_path

    def initialize_dynamic_settings(self):
        """Initizliez settings that change throughout the game"""
        self.ship_speed = 3.5
        self.bullet_speed = 3.0
        self.alien_speed = 7.0


        # fleet_direction of 1 represents right and -1 repressents left
        self.fleet_direction = 1

        #SCoring 
        self.alien_points= 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
