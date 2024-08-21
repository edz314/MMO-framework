# src/ai/actions/roar.py

from .action import Action

class RoarAction(Action):
    def __init__(self):
        super().__init__(name="Roar", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is roaring to intimidate enemies!")
        # Implement logic to roar, potentially intimidating enemies or boosting allies
        enemies = environment.get_nearby_enemies(npc)
        for enemy in enemies:
            enemy.intimidated_by(npc)
        npc.boost_morale()
