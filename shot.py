import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen, camera_offset_y=0):
        offset_pos = pygame.Vector2(self.position.x, self.position.y - camera_offset_y)
        pygame.draw.circle(screen, (255, 255, 255), offset_pos, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt