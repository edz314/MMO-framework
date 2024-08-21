# src/ai/actions/attack.py

from .action import Action

class AttackAction(Action):
    def __init__(self):
        super().__init__(name="Attack", prerequisites=["Weapon"])

    def execute(self, npc, environment):
        print(f"{npc.name} attacks the enemy!")
        # Implement attack logic here
