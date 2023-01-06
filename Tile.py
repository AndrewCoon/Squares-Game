class Tile:
    state = None
    occupied = None

    def __init__(self):
        self.occupied = False
        self.state = 0

    def __int__(self):
        return self.state

    def __str__(self):
        return str(self.state)

    def change_state(self, state):
        self.state = state

        print(f'state changed to {self.state}')
        if self.state == 0:
            self.occupied = False
        else:
            self.occupied = True
