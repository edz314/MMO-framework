# src/ai/actions/greet.py

from .action import Action

class GreetAction(Action):
    def __init__(self):
        super().__init__(name="Greet", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is greeting a nearby NPC!")
        # Implement logic to greet another NPC
        nearby_npc = environment.get_nearby_npc(npc)
        if nearby_npc:
            npc.greet(nearby_npc)
