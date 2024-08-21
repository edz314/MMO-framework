# src/ai/actions/retreat.py

from .action import Action

class RetreatAction(Action):
    def __init__(self):
        super().__init__(name="Retreat", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is retreating from battle!")
        # Implement logic to retreat to a safe location
        safe_zone = environment.find_safe_zone(npc)
        npc.move_to(safe_zone)
