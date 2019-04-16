import pygame
from bullet import Bullet


class Player:
    """Make an object of Player"""
    def __init__(self, pid, x, y, width, height, color, bullet_dir=1):
        self.pid = pid  # player id
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.velocity = 7
        self.health = 3
        self.is_destroy = False
        self.is_fire = False
        self.bullet = None
        self.dir = bullet_dir

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def damaged(self, val=1):
        hp = self.health - val
        if hp <= 0:
            self.health = 0
            self.is_destroy = True
        else:
            self.health = hp

    def update(self, bounds):
        keys = pygame.key.get_pressed()
        bound_left = bounds[0]
        bound_right = bounds[1] - self.width

        if not self.is_destroy:
            if keys[pygame.K_LEFT] and self.x > bound_left:
                self.x -= self.velocity
            elif keys[pygame.K_RIGHT] and self.x < bound_right:
                self.x += self.velocity

            if keys[pygame.K_SPACE] and not self.is_fire:
                self.bullet = self.shoot()
                self.is_fire = True

        if self.is_fire and self.bullet:
            if (self.bullet.y < bounds[1]) and (self.bullet.y > bounds[0]):
                self.bullet.update()
            else:
                del self.bullet
                print('Deleted bullet from pid: {}'.format(self.pid))
                self.is_fire = False

        self.draw_update()

    def shoot(self):
        return Bullet(self)

    def draw_update(self):
        self.rect = (self.x, self.y, self.width, self.height)
