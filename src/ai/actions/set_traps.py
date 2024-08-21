# src/ai/actions/set_traps.py

from .action import Action

class SetTrapsAction(Action):
    def __init__(self):
        super().__init__(name="Set Traps", prerequisites=["Trap"])

    def execute(self, npc, environment):
        print(f"{npc.name} is setting traps in the area.")
        # Implement logic to set traps in strategic locations
        trap_locations = environment.get_trap_locations(npc)
        for location in trap_locations:
            npc.set_trap(location)
