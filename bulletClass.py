class Bullet:
    bulletList = []
    def __init__(self, cx, cy, dir):
        self.cx = cx
        self.cy = cy
        self.dir = dir
        self.hasBounced = False
        self.steps = 0
        self.destroy = False
        Bullet.bulletList.append(self)
    
    def __repr__(self):
        return f'Bullet(cx={self.cx}, cy={self.cy})'
    
    def __eq__(self, other):
        return (isinstance(other, Bullet) and 
                self.cx == other.cx and 
                self.cy == other.cy)
    
    def move(self):
        if self.dir == 1:
            if self.steps % 2:
                self.cx -= 1
            else:
                self.cy -= 1
        elif self.dir == 2:
            self.cy -= 1
        elif self.dir == 3:
            if self.steps % 2:
                self.cx += 1
            else:
                self.cy -= 1
        elif self.dir == 4:
            self.cx -= 1
        elif self.dir == -4:
            self.cx += 1
        elif self.dir == -1:
            if self.steps % 2:
                self.cx -= 1
            else:
                self.cy += 1
        elif self.dir == -2:
            self.cy += 1
        else:
            if self.steps % 2:
                self.cx += 1
            else:
                self.cy += 1
    
    def step(self):
        self.steps += 1
        self.move()
    
    def bounce(self):
        if not self.hasBounced:
            self.dir = -self.dir
            self.hasBounced = True
        else:
            self.destroy = True
    

b1 = Bullet(150, 150, -2)
print(str(b1))