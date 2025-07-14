import pygame
import random
from circleshape import CircleShape
from constants import *


class Oil(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= OIL_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(random_angle) * 1.2
            vel2 = self.velocity.rotate(-random_angle) * 1.2
            new_radius = self.radius - OIL_MIN_RADIUS
            oil1 = Oil(self.position.x, self.position.y, new_radius)
            oil2 = Oil(self.position.x, self.position.y, new_radius)
            oil1.velocity = vel1
            oil2.velocity = vel2
            return oil1, oil2