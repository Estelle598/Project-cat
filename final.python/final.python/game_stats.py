class GameStats:
    """Track stats for the game"""

    def __init__(self, ai_game):
        """Initiate stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        #Start the game in an inactive state
        self.game_active = False

        #High score should not be reset
        self.high_score =0



    def reset_stats(self):
        """Initialize stats that can chang eduring the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1