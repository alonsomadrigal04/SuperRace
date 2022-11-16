class GameState:
    def __init__(self):
        self.track = None
        self.player_position_row = 0
        self.player_position_colum = 0
        self.velocity = 1


    def reset(self, track):
        """Initialize the Gmae State"""
        self.track = track
        self.player_position_row, self.player_position_colum = track.get_initial_position()
        self.velocity = 1

        def get_player_position(self):
            return [self.player_position_row, self.player_position_colum]

        def set_player_postion(self, row, colum):
            self.player_position_row = row
            self.player_position_colum = colum

        def __str__(self):
            s = ""
            s += "Player Position" + str(set_player_postion())
            s += "Velocity" + self(self.velocity)
            s += "Track" + self.track.print_track(self.player_position_row, self.player_position_colum)

