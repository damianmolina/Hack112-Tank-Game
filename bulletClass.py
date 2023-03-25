class Bullet:
    bulletCount = 0
    def __init__(self, cx, cy, dir):
        if Bullet.bulletCount <= 2:
            self.cx = cx
            self.cy = cy
            self.dir = dir
            self.hasBounced = False
            self.steps = 0
            Bullet.bulletCount += 1
            self.destory = False
    
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
    
    def onStep(self):
        self.steps += 1
        self.move()

    def hasCollided(self):
        if not 25 < self.cx < 575:
            if not self.hasBounced:
                self.hasBounced = True
                self.dir = -self.dir
            else:
                self.destroy = True
                Bullet.bulletCount -= 1     
        if not 125 < self.cy < 575:
            if not self.hasBounced:
                self.hasBounced = True
                self.dir = -self.dir  
            else:
                self.destroy = True
                Bullet.bulleCount -= 1         


            
