import pygame
from circleshape import CircleShape
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
        self.timer = 0
        self.depth = self.position.y
    
    def draw(self, screen, camera_offset_y=0):
        offset_points = [pygame.Vector2(self.position.x, self.position.y - camera_offset_y) for self.position in self.triangle()]
        pygame.draw.polygon(screen, (255, 255, 255), offset_points, 2)

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt
            if self.timer < 0:
                self.timer = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
           #A key pressed
            self.rotate(-dt)
        if keys[pygame.K_d]:
            #D key pressed
            self.rotate(dt)
        if keys[pygame.K_s]:
            #S key pressed
            self.move(-dt)
        if keys[pygame.K_w]:
            #W key pressed
            self.move(dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
                self.shoot()
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN