#!/usr/bin/env python3
from components import consumable
from components.ai import HostileEnemy
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item


player = Actor(char="@",
               color=(255, 255, 255),
               name="Player",
               ai_cls=HostileEnemy,
               fighter=Fighter(hp=30, defense=2, power=5),
               inventory=Inventory(capacity=26),
               level=Level(level_up_base=200),
               )

# monsters
orc = Actor(char="o",
            color=(63, 127, 63),
            name="Orc",
            ai_cls=HostileEnemy,
            fighter=Fighter(hp=10, defense=0, power=3),
            inventory=Inventory(capacity=0),
            level=Level(xp_given=20),
            )

kobold = Actor(
    char="k",
    color=(0, 127, 254),
    name="Kobold",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=5, defense=1, power=2),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=10),
)

troll = Actor(char="T",
              color=(0, 127, 0),
              name="Troll",
              ai_cls=HostileEnemy,
              fighter=Fighter(hp=16, defense=1, power=4),
              inventory=Inventory(capacity=0),
              level=Level(xp_given=50),
              )

# items
health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(max_amount=8),
)

lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

confusion_scroll = Item(
    char="~",
    color=(0, 255, 10),
    name="Scroll of Confusion",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)

fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3)
)
