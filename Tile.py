class Tile:
    state = None
    occupied = None

    def __init__(self):
        self.occupied = False
        # self.state = 0

    def __int__(self):
        update_state()
        return self.state

    def __str__(self):
        update_state()
        return str(self.state)

    def update_state(self, ):
        if self.state == 0:
            self.occupied = False
        else:
            self.occupied = True
