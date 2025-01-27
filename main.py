import pygame
import sys
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    FPS = 60
    dt = 0
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable) 
    
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updateable, drawable)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for upd in updateable:
            upd.update(dt)
        
        screen.fill("black")

        for ast in asteroids:
            if ast.collision(player):
                print("Game Over")
                sys.exit()
            
            for bullet in shots:
                if ast.collision(bullet):
                    ast.split()
                    bullet.kill()

        for drw in drawable:
            drw.draw(screen)
        
        
        pygame.display.flip()

        

        dt = game_clock.tick(FPS)/1000

if __name__ == "__main__":
    main()