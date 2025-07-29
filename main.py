import pygame
import sys
from constants import *
from player import Player
from oil import Oil
from oilfield import *
from shot import *

def main():
    pygame.init()
    print("Starting Deep Blue Defender!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up the window and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Sprite groups – like toy bins for organizing who updates and draws
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    oil_blobs = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Place the player in the middle of the screen
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = (updatable, drawable)
    player = Player(x, y)

    # Oil blobs and the oilfield
    Oil.containers = (oil_blobs, updatable, drawable)
    OilField.containers = (updatable,)
    Oilfield = OilField()

    # Set up shooting
    Shot.containers = (shots, updatable, drawable)

    # Set up oil spawn timing
    spawn_timer = 0
    spawn_interval = 3  # seconds


    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BACKGROUND_COLOR)
        updatable.update(dt)   

        for oil in oil_blobs:
            if player.collision(oil):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.collision(oil):
                    shot.kill()
                    new_oil_blobs = oil.split()
                    if new_oil_blobs:
                        oil_blobs.add(new_oil_blobs[0], new_oil_blobs[1])
                        updatable.add(new_oil_blobs[0], new_oil_blobs[1])
                        drawable.add(new_oil_blobs[0], new_oil_blobs[1])

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
