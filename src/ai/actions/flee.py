# src/ai/actions/flee.py

from .action import Action

class FleeAction(Action):
    def __init__(self):
        super().__init__(name="Flee", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} flees from danger!")
        # Implement fleeing logic here
