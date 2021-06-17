
import numpy as np  # type: ignore
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height),
                             fill_value=tile_types.wall,
                             order="F")
        # tiles the player can see:
        self.visible = np.full((width, height), fill_value=False, order="F")
        # tiles the player can't see:
        self.explored = np.full((width, height), fill_value=False, order="F")

    def in_bounds(self, x: int, y: int) -> bool:
        '''returns True if x and y are inside the bounds of this map'''
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
