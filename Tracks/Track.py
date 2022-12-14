class Track:
    def __int__(self):
        self.track = [[0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                      [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                      [0, 0, 1, 1, 1, 1, 1, 0, 0, 0]]
        self.number_of_rows = len(self.track)
        self.number_of_columns = len(self.track[0])

    def get_initial_position(self):
        """Return the initial position of the player"""
        return 5, 4

    def is_goal(self, row, column):
        """Return True if the given position is the goal position"""
        return row == 0 and column in [2, 3, 4, 5]

    def print_track(self, row, column):
        s = ""
        for r in range(self.number_of_rows):
            for c in range(self.number_of_columns):
                if r == row and c == column:
                    s += "X"
                elif self.track[r][c] == 1:
                    s += " "
                else:
                    s += "#"
        return s