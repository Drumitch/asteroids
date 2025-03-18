import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Objects
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    black = (0, 0, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Generates a black screen
        screen.fill(black)

        # Generates the player sprite
        for sprite in drawable:
            sprite.draw(screen)

        # Refreshes the screen
        pygame.display.flip()

        # Calls the update method, turning the player ship
        for up in updatable:
            up.update(dt)

        # Checks for asteroid-player collision and ends the game if True
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                pygame.time.delay(2000)
                pygame.quit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        # Limits the refresh rate to 60 fps
        dt = game_clock.tick(60) / 1000
print("Starting Asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()