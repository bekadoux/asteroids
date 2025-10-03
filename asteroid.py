import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_VEL_SCALE_ON_SPLIT


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, field):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50 + 0.01)
        v1, v2 = self.velocity.rotate(angle), self.velocity.rotate(-angle)
        v1 *= ASTEROID_VEL_SCALE_ON_SPLIT
        v2 *= ASTEROID_VEL_SCALE_ON_SPLIT
        split_asteroid_r = self.radius - ASTEROID_MIN_RADIUS

        field.spawn(split_asteroid_r, self.position, v1)
        field.spawn(split_asteroid_r, self.position, v2)
