# src/ai/actions/alert_allies.py

from .action import Action

class AlertAlliesAction(Action):
    def __init__(self):
        super().__init__(name="Alert Allies", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is alerting allies!")
        # Implement logic to notify nearby allies
        for ally in environment.get_nearby_allies(npc):
            ally.receive_alert(npc)
