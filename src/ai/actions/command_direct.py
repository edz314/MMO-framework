# src/ai/actions/command_direct.py

from .action import Action

class CommandDirectAction(Action):
    def __init__(self):
        super().__init__(name="Command Direct", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is issuing direct commands!")
        # Implement logic for the NPC to issue direct orders to nearby allies
        for ally in environment.get_nearby_allies(npc):
            ally.receive_command(npc)
