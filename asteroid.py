from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, updatable_group, drawable_group, asteroid_group):
        super().__init__(x, y, radius)
        self.radius = radius
        self.x = x
        self.y = y
        self.updatable_group = updatable_group
        self.drawable_group = drawable_group
        self.asteroid_group = asteroid_group
        self.add(self.updatable_group, self.drawable_group, self.asteroid_group)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        print("Asteroid split method called!")
        self.kill()
        print(f"Asteroid radius: {self.radius}, Min radius: {ASTEROID_MIN_RADIUS}")
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid1 = Asteroid(
            self.position.x, self.position.y, new_radius,
            self.updatable_group, self.drawable_group, self.asteroid_group
                                   )
        split_asteroid2 = Asteroid(
            self.position.x, self.position.y, new_radius,
            self.updatable_group, self.drawable_group, self.asteroid_group
            )
        print("New asteroids created!")
        print(f"Parent velocity magnitude: {self.velocity.length()}")
        split_asteroid1.velocity = new_velocity1 * 1.2
        split_asteroid2.velocity = new_velocity2 * 1.2

        

        
    