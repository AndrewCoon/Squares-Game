class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupied = False

    def pos(self):
        return self.x, self.y
