import pygame
from constants import *
import player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player_character = player.Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color=(0, 0, 0))        
        player_character.update(dt)
        player_character.draw(screen)
        pygame.display.flip()
        dt = (clock.tick(60)/1000)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
