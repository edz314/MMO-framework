# src/ai/fsm/npc_mind_type_fsm.py

from src.ai.fsm.fsm_controller import FSMController
from src.data.npc_data import NPCData

class NPCMindTypeFSM(FSMController):
    def __init__(self, npc_data):
        super().__init__()
        self.npc_data = npc_data

    def has_required_items(self, mind_type):
        """
        Check if the NPC has the required items for the specified mind type.
        :param mind_type: The mind type to check against.
        :return: True if all required items are present, otherwise False.
        """
        required_items = mind_types.get(mind_type, {}).get('required_items', [])
        for item in required_items:
            if item not in self.npc_data.inventory:
                return False
        return True

    def switch_mind_type(self, new_mind_type):
        """
        Switch the NPC's mind type if they have the required items.
        :param new_mind_type: The mind type to switch to.
        """
        if self.has_required_items(new_mind_type):
            self.npc_data.current_mind_type = new_mind_type
            print(f"{self.npc_data.name} has switched to {new_mind_type} mind type.")
        else:
            print(f"{self.npc_data.name} cannot switch to {new_mind_type} mind type due to missing required items.")

    def update(self, environment):
        """
        Update the FSM based on the current mind type and environment.
        :param environment: The environment in which the NPC operates.
        """
        mind_type = self.npc_data.current_mind_type
        self.transition_to(mind_type)
        self.execute_state(self.npc_data, environment)

# Example usage:
npc_data = NPCData(name="Archer 1", inventory=["bow", "arrows"])
npc_fsm = NPCMindTypeFSM(npc_data)
npc_fsm.switch_mind_type("Archer")
npc_fsm.update(environment)
