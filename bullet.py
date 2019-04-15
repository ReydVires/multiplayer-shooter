import pygame


class Bullet:
    def __init__(self, player, dir):
        self.width = player.width * .1
        self.height = player.height * .5
        self.x = player.x + (player.width * .5) - (self.width * .5)
        self.y = player.y + (dir * player.height * .5)
        self.diff_color = 50 * dir
        self.color = (200 + self.diff_color, 55, 50 + self.diff_color)
        self.rect = (self.x, self.y, self.width, self.height)
        self.shot_speed = 12 * dir
        print('bullet created', self.rect)
        self.dir = dir

    def update(self, win):
        self.y = self.y + self.shot_speed
        self.draw_update()
        print('Check y:', self.y, 'x:', self.x)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def draw_update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def is_collided_with(self, win, obj):
        if (self.x >= obj.x) and (self.x <= (obj.x + obj.width)) and not obj.is_destroy:
            if self.dir == 1 and (self.y + self.height/2) > (obj.y - obj.height/2):
                self.y = 500
                return True
            elif self.dir == -1 and (self.y + self.height/2) < (obj.y + obj.height/2):  # if top
                self.y = -10
                return True
        return False
