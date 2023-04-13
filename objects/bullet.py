class Bullet:
    def __init__(self, c, tx, ty, image, color):
        self.tx = tx
        self.ty = ty
        self.image = image
        self.color = color
        self.canvas = c

    @property
    def x(self):
        return self.canvas.coords(self.image)[0]

    @property
    def y(self):
        return self.canvas.coords(self.image)[1]

    def is_finished(self):
         return int(self.tx) <= int(self.x) and int(self.tx) + 136 > int(self.x) and int(self.ty) >= int(self.y) and int(self.ty) + 136 >= int(self.y)