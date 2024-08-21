# src/ai/actions/chase.py

from .action import Action

class ChaseAction(Action):
    def __init__(self):
        super().__init__(name="Chase", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is chasing a target!")
        # Implement logic to chase a specific target
        target = environment.get_closest_enemy(npc)
        if target:
            npc.move_towards(target)
