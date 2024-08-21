# src/ai/actions/examine.py

from .action import Action

class ExamineAction(Action):
    def __init__(self):
        super().__init__(name="Examine", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is examining the surroundings!")
        # Implement logic for the NPC to examine the environment for information
        details = environment.examine_area(npc.position)
        npc.analyze_information(details)
