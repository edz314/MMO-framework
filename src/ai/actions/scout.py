# src/ai/actions/scout.py

from .action import Action

class ScoutAction(Action):
    def __init__(self):
        super().__init__(name="Scout", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is scouting the area ahead.")
        # Implement logic to scout and report back findings
        scout_area = environment.determine_scout_area(npc)
        npc.scout_area(scout_area)
        npc.report_back(scout_area)
