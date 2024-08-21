# src/ai/actions/coordinate_with_allies.py

from .action import Action

class CoordinateWithAlliesAction(Action):
    def __init__(self):
        super().__init__(name="Coordinate With Allies", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is coordinating with allies!")
        # Implement logic for the NPC to plan actions with nearby allies
        for ally in environment.get_nearby_allies(npc):
            ally.coordinate_strategy(npc)
