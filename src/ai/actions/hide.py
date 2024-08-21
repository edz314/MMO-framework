# src/ai/actions/hide.py

from .action import Action

class HideAction(Action):
    def __init__(self):
        super().__init__(name="Hide", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is hiding from enemies!")
        # Implement logic to find and move to a hiding spot
        hiding_spot = environment.find_hiding_spot(npc)
        if hiding_spot:
            npc.move_to(hiding_spot)
