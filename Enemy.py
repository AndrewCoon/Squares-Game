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
        return (self.x-other.x, self.y-other.y)

    def move(self, dist, px, py):
        i = 0
        while (i < dist):
            if (px > self.x):
                x -= 1
                i += 1
                break
            elif (px < self.x):
                x += 1
                i += 1
                break
            if (py > self.y):
                y -= 1
                i += 1
                break
            elif (py < self.y):
                y += 1
                i += 1
                break
