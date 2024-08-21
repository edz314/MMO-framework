# src/ai/actions/beg_for_mercy.py

from .action import Action

class BegForMercyAction(Action):
    def __init__(self):
        super().__init__(name="Beg For Mercy", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is begging for mercy!")
        # Implement logic to beg for mercy, perhaps affecting enemy behavior
        if environment.is_enemy_nearby(npc):
            enemy = environment.get_closest_enemy(npc)
            enemy.consider_mercy(npc)
