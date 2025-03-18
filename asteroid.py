import pygame
import random
from circleshape import CircleShape
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPAWN_RATE
)

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        yellow = (255, 251, 0)
        orange = (255, 101, 0)
        red = (230, 0, 0)
        if self.radius == ASTEROID_MIN_RADIUS:
            pygame.draw.circle(screen, yellow, self.position, self.radius, 2)
        elif self.radius == ASTEROID_MAX_RADIUS:
            pygame.draw.circle(screen, red, self.position, self.radius, 2)
        else:
            pygame.draw.circle(screen, orange, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20, 50)
        new_vect1 = self.velocity.rotate(rand_angle)
        new_vect2 = self.velocity.rotate(-rand_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        split1 = Asteroid(self.position.x, self.position.y, new_rad)
        split2 = Asteroid(self.position.x, self.position.y, new_rad)
        split1.velocity = new_vect1 * 1.2
        split2.velocity = new_vect2 * 1.2