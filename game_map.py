#!/usr/bin/env python3
from __future__ import annotations

from typing import Iterable, Iterator, Optional, TYPE_CHECKING

import numpy as np  # type: ignore
from tcod.console import Console

from entity import Actor
import tile_types

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class GameMap:
    def __init__(self,
                 engine: Engine,
                 width: int,
                 height: int,
                 entities: Iterable[Entity] = ()):
        self.engine = engine
        self.width, self.height = width, height
        self.entities = set(entities)
        self.tiles = np.full((width, height),
                             fill_value=tile_types.wall,
                             order="F")
        # tiles the player can see:
        self.visible = np.full((width, height), fill_value=False, order="F")
        # tiles the player has already seen:
        self.explored = np.full((width, height), fill_value=False, order="F")
    
    @property
    def actors(self) -> Iterator[Actor]:
        """ Iterate over this map's living actors """
        yield from(
            entity
            for entity in self.entities
            if isinstance(entity, Actor) and entity.is_alive
        )

    def get_block_at_dest(self,
                          location_x: int,
                          location_y: int) -> Optional[Entity]:
        for entity in self.entities:
            if entity.blocks_movement and entity.x == location_x and \
                    entity.y == location_y:
                return entity

        return None

    def get_actor_at_location(self, x: int, y: int) -> Optional[Actor]:
        for actor in self.actors:
            if actor.x == x and actor.y == y:
                return actor

        return None

    def in_bounds(self, x: int, y: int) -> bool:
        '''returns True if x and y are inside the bounds of this map'''
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.

        tiles in the 'visible' array are drawn with 'light' colors.
        nonvisible but explored tiles are drawn with the 'dark colors'
        otherwise default to SHROUD.
        """
        # console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD,
        )

        for entity in self.entities:
            # Only print entities in current Field of View
            if self.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg=entity.color)
