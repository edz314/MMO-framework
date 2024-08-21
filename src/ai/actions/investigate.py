# src/ai/actions/investigate.py

from .action import Action

class InvestigateAction(Action):
    def __init__(self):
        super().__init__(name="Investigate", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is investigating an area!")
        # Implement logic to investigate a suspicious area or event
        target_area = environment.find_suspicious_area(npc)
        if target_area:
            npc.move_to(target_area)
            npc.examine_area(target_area)
