import pygame


class Bullet:
    def __init__(self, player):
        self.width = player.width * .1
        self.height = player.height * .5
        self.x = player.x + (player.width * .5) - (self.width * .5)
        self.y = player.y + (player.dir * player.height * .5)
        self.diff_color = 50 * player.dir
        self.color = (200 + self.diff_color, 55 - self.diff_color, 50 + self.diff_color)
        self.rect = (self.x, self.y, self.width, self.height)
        self.shot_speed = 12 * player.dir
        print('bullet created', self.rect)
        self.pid = player.pid

    def update(self):
        self.y = self.y + self.shot_speed
        self.draw_update()
        print('Check y:', self.y, 'x:', self.x)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def draw_update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def is_collided_with(self, obj):
        if (self.x >= obj.x) and (self.x <= (obj.x + obj.width)) and not obj.is_destroy:
            # if player 1
            if self.pid == 0 and (self.y + self.height/2) > (obj.y - obj.height/2):
                self.y = 500  # make it destroy because out of screen
                return True
            # if player 2
            elif self.pid == 1 and (self.y + self.height/2) < (obj.y + obj.height):  # if top
                self.y = -10  # make it destroy because out of screen
                return True
        return False
