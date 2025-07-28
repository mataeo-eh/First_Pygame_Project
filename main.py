import pygame
import sys
from constants import * 
from circleshape import *
from player import *
from asteroid import *
from asteroid_field import *
from bullet import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroid = pygame.sprite.Group()
bullots_shot = pygame.sprite.Group()
Bullet.containers = (bullots_shot, updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroid)
Player.containers = (updatable, drawable)
AsteroidField.containers = (updatable)

def main():
    pygame.init()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    clock = pygame.time.Clock()
    asteroid_field = AsteroidField(updatable, drawable, asteroid)
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawables in drawable:
            drawables.draw(screen)
        updatable.update(dt)
        for asteroids in asteroid:
            if asteroids.collisions(player.position) < asteroids.radius + player.radius:
                sys.exit("Game over!")
        for bullets in bullots_shot:
            for asteroids in asteroid:
             if bullets.collisions(asteroids.position) < asteroids.radius + bullets.radius:
                asteroids.split()
                bullets.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000
    print("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
