import pytest

from game_controllers.pacman_game_controller import PacmanGameController
from utils.pathfinder import Pathfinder


@pytest.fixture
def pathfinder():
    pacman_game = PacmanGameController()
    return Pathfinder(pacman_game.numpy_maze)

@pytest.mark.parametrize("from_x,from_y,to_x,to_y,expected", [
    (1, 1, 2, 1, [(1, 2)]),
    (1, 1, 10, 1, [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (6, 8), (6, 9), (6, 10), (5, 10), (4, 10), (3, 10), (2, 10), (1, 10)]),
    (1, 1, 1, 10, [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)]),
])
def test_path_finder(pathfinder, from_x, from_y, to_x, to_y, expected):
    print(pathfinder.get_path(from_x, from_y, to_x, to_y))
    assert pathfinder.get_path(from_x, from_y, to_x, to_y) == expected
