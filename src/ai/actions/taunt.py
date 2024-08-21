# src/ai/actions/taunt.py

from .action import Action

class TauntAction(Action):
    def __init__(self):
        super().__init__(name="Taunt", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is taunting the enemy.")
        # Implement logic to taunt enemies, possibly provoking them
        enemy = environment.get_closest_enemy(npc)
        if enemy:
            npc.taunt(enemy)
