import pytest

from game_controllers.game_renderer import GameRenderer
from game_controllers.pacman_game_controller import PacmanGameController
from game_objects.impl.hero import Hero
from game_objects.impl.wall import Wall


@pytest.fixture
def hero():
    unified_size = 32
    pacman_game = PacmanGameController()
    size = pacman_game.size
    game_renderer = GameRenderer(size[0] * unified_size, size[1] * unified_size)
    for y, row in enumerate(pacman_game.numpy_maze):
        for x, column in enumerate(row):
            if column == 0:
                game_renderer.add_wall(Wall(game_renderer, x, y, unified_size))
    pacman = Hero(game_renderer, unified_size, unified_size, unified_size)
    return pacman

@pytest.mark.parametrize("position,expected", [
    ((64, 32), False),
    ((64, 64), True),
    ((32, 32), False),
    ((96, 96), True),
    ((96, 32), False),
])
def test_collides_with_wall(hero, position, expected):
    assert hero.collides_with_wall(position) == expected