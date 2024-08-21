# src/ai/actions/cover.py

from .action import Action

class CoverAction(Action):
    def __init__(self):
        super().__init__(name="Cover", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is taking cover!")
        # Implement logic for the NPC to find and move to cover
        cover_spot = environment.find_nearest_cover(npc)
        if cover_spot:
            npc.move_to(cover_spot)
