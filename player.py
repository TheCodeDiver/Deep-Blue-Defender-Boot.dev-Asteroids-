import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)


        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        print(f"Rotating by {PLAYER_TURN_SPEED * dt}")  # This will display how much rotation is added each time
        self.rotation += PLAYER_TURN_SPEED * dt
        print(f"New rotation: {self.rotation}")

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            print("A key pressed!")
            self.rotate(-dt)
        if keys[pygame.K_d]:
            print("D key pressed!")
            self.rotate(dt)
        if keys[pygame.K_s]:
            print("S key pressed!")
            self.move(-dt)
        if keys[pygame.K_w]:
            print("W key pressed!")
            self.move(dt)

        
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt