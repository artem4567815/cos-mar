class Block:
    def __init__(self, c, image, color, is_bullet):
        self.image = image
        self.color = color
        self.canvas = c
        self.is_bullet = is_bullet

    @property
    def x(self):
        return self.canvas.coords(self.image)[0]

    @property
    def y(self):
        return self.canvas.coords(self.image)[1]