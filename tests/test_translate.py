from utils.translate import translate_screen_to_maze, translate_maze_to_screen
import pytest


# Тесты для translate_screen_to_maze
@pytest.mark.parametrize("in_coords, in_size, expected", [
    ((64, 64), 32, (2, 2)),
    ((0, 0), 32, (0, 0)),
    ((31, 31), 32, (0, 0)),  # Граничные условия
    ((33, 33), 32, (1, 1)),  # Чуть выше граничного значения
    ((96, 64), 32, (3, 2)),  # Произвольные значения
    ((64, 64), 16, (4, 4)),  # Измененный размер ячейки
])
def test_translate_screen_to_maze(in_coords, in_size, expected):
    assert translate_screen_to_maze(in_coords, in_size) == expected

# Тесты для translate_maze_to_screen
@pytest.mark.parametrize("in_coords, in_size, expected", [
    ((2, 2), 32, (64, 64)),
    ((0, 0), 32, (0, 0)),
    ((1, 1), 32, (32, 32)),
    ((3, 2), 32, (96, 64)),
    ((4, 4), 16, (64, 64)),  # Измененный размер ячейки
])
def test_translate_maze_to_screen(in_coords, in_size, expected):
    assert translate_maze_to_screen(in_coords, in_size) == expected
