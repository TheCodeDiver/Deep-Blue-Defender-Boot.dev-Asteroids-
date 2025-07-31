import pygame
import random
from circleshape import CircleShape
from constants import *


class Oil(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        angle = random.uniform(-30, 30) #side drift
        speed = random.uniform(30, 60) #lazy drift
        self.velocity = pygame.Vector2(0, speed).rotate(angle)
        
    def draw(self, screen, camera_offset_y=0):
        offset_points = pygame.Vector2(self.position.x, self.position.y - camera_offset_y)
        # outer dark blob
        pygame.draw.circle(screen, (30, 30, 30), offset_points, self.radius, 2)
        # inner rim
        pygame.draw.circle(screen, (10, 10, 10), offset_points, max(self.radius - 3, 1), 1)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= OIL_MIN_RADIUS:
            bubble_pop(self.position.x, self.position.y)
            return None
        
        random_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - OIL_MIN_RADIUS
        oil1 = Oil(self.position.x, self.position.y, new_radius)
        oil2 = Oil(self.position.x, self.position.y, new_radius)
        oil1.velocity = vel1
        oil2.velocity = vel2
        return oil1, oil2
    
    
def bubble_pop(x, y):
    print(f"Bubble Pop at ({x}, {y})")