# src/ai/actions/call.py

from .action import Action

class CallAction(Action):
    def __init__(self):
        super().__init__(name="Call", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is calling for assistance!")
        # Implement logic to broadcast a call for help to nearby allies
        for ally in environment.get_nearby_allies(npc):
            ally.respond_to_call(npc)
