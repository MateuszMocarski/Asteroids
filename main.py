import pygame
from player import Player
from constants import *

def main():
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    FPS = 60
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for upd in updateable:
            upd.update(dt)
        
        screen.fill("black")

        for drw in drawable:
            drw.draw(screen)
        
        
        pygame.display.flip()

        

        dt = game_clock.tick(FPS)/1000

if __name__ == "__main__":
    main()