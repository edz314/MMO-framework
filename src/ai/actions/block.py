# src/ai/actions/block.py

from .action import Action

class BlockAction(Action):
    def __init__(self):
        super().__init__(name="Block", prerequisites=["Shield"])

    def execute(self, npc, environment):
        print(f"{npc.name} is blocking with a shield!")
        # Implement blocking logic, reducing or negating incoming damage
        if npc.is_under_attack():
            npc.reduce_incoming_damage()
