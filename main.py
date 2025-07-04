import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)
    

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)   

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    new_asteroids = asteroid.split()
                    if new_asteroids:
                        asteroids.add(new_asteroids[0], new_asteroids[1])
                        updatable.add(new_asteroids[0], new_asteroids[1])
                        drawable.add(new_asteroids[0], new_asteroids[1])

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
