import pygame
import constants as c
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():    
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    character = Player((c.SCREEN_WIDTH / 2), (c.SCREEN_HEIGHT / 2))
    field = AsteroidField()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color=(0, 0, 0))    
        for entity in updatable:
            entity.update(dt)
        for entity in drawable:
            entity.draw(screen)
        for entity in asteroids:
            for shot in shots:
                if entity.check_collision(shot):
                    entity.split()
                    shot.kill()
            if entity.check_collision(character):
                print("Game over!")
                return

        pygame.display.flip()
        dt = (clock.tick(60)/1000)
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
