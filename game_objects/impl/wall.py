from game_objects.game_object import GameObject


class Wall(GameObject):
    def __init__(self, in_surface, x, y, in_size: int, in_color=(0, 138, 6)):
        super().__init__(in_surface, x * in_size, y * in_size, in_size, in_color)