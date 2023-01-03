class Enemie:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(speed, px, py):
        i = 0
        while (i < speed):
            if (px > x):
                x -= 1
                i += 1
                break
            elif (px < x):
                x += 1
                i += 1
                break
            if (py > x):
                y -= 1
                i += 1
                break
            elif (py < x):
                y += 1
                i += 1
                break
