from circleshape import CircleShape
from constants import PLAYER_SHOOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SHOOT_RADIUS)
