# src/ai/actions/move_slowly.py

from .action import Action

class MoveSlowlyAction(Action):
    def __init__(self):
        super().__init__(name="Move Slowly", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is moving slowly to avoid detection!")
        # Implement logic to move slowly, reducing noise or visibility
        npc.set_movement_speed(slow=True)
        npc.move_to(environment.get_target_location(npc))
