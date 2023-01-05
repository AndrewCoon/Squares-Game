class Enemy:
    # previous x, y
    prex, prey = 0, 0

    def __init__(self, x=False, y=False):
        if not x:
            self.x = 5
        else:
            self.x = x

        if not y:
            self.y = 5
        else:
            self.y = y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def move(self, dist, px, py):
        i = 0
        while i < dist:
            if px > self.x:
                self.x += 1
                i += 1
            elif px < self.x:
                self.x -= 1
                i += 1
            if py > self.y:
                self.y += 1
                i += 1
            elif py < self.y:
                self.y -= 1
                i += 1

    def pos(self):
        return self.x, self.y
