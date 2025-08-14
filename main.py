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

    camera_offset_y = 0
    DESCENT_TRIGGER_Y = SCREEN_HEIGHT * 0.75 # Position to trigger scrolling


    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        depth = camera_offset_y
        max_depth = 5000

        #calculate darkness per depth
        darkness = min(depth / max_depth, 1.0)
        bg_color = (
            int(0 * (1 - darkness) + 0 * darkness), #red
            int(105 * (1 - darkness) + 0 * darkness), #green
            int(148 * (1 - darkness) + 30 * darkness), #blue
        )
        screen.fill(bg_color)

        font = pygame.font.SysFont(None, 36)
        depth_text = font.render(f"Depth: {int(depth)}", True, (255, 255, 255))
        screen.blit(depth_text, (10, 10))


        player.update(dt, camera_offset_y)
        for sprite in updatable:
            if sprite != player:
                sprite.update(dt)

        # Scrolling depth
        keys = pygame.key.get_pressed()
        moving_down = keys[pygame.K_w]  # The player is pressing the "go forward" key

        # Only scroll if the player is pushing forward AND they're past the descent trigger
        if moving_down and player.position.y - camera_offset_y > DESCENT_TRIGGER_Y:
            descent_speed = PLAYER_SPEED * dt
            camera_offset_y += descent_speed
            player.position.y -= descent_speed  # Lock them from escaping upward


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
            sprite.draw(screen, camera_offset_y)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        print(f"Player Y: {player.position.y:.2f}, Camera Offset Y: {camera_offset_y:.2f}")
        print(f"Player X: {player.position.x:.2f}, Y: {player.position.y:.2f}, Camera Offset Y: {camera_offset_y:.2f}")





if __name__ == "__main__":
    main()
