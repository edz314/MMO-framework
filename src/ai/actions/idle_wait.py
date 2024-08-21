# src/ai/actions/idle_wait.py

from .action import Action

class IdleWaitAction(Action):
    def __init__(self):
        super().__init__(name="Idle Wait", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is idling and waiting...")
        # Implement logic for the NPC to idle or wait
        npc.idle()
