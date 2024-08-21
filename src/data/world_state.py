# src/data/world_state.py

class WorldState:
    def __init__(self):
        """
        Initialize the WorldState with default values.
        """
        self.npc_positions = {}  # Dictionary to store NPC positions
        self.environmental_conditions = {}  # Dictionary to store environmental conditions

    def update_npc_position(self, npc_name, position):
        """
        Update the position of a specific NPC in the world.
        :param npc_name: The name of the NPC.
        :param position: A tuple representing the NPC's new position (x, y).
        """
        self.npc_positions[npc_name] = position

    def get_npc_position(self, npc_name):
        """
        Get the current position of a specific NPC.
        :param npc_name: The name of the NPC.
        :return: A tuple representing the NPC's current position, or None if the NPC is not found.
        """
        return self.npc_positions.get(npc_name)

    def update_environmental_condition(self, condition_name, value):
        """
        Update a specific environmental condition in the world.
        :param condition_name: The name of the environmental condition (e.g., "weather", "time_of_day").
        :param value: The new value for the condition.
        """
        self.environmental_conditions[condition_name] = value

    def get_environmental_condition(self, condition_name):
        """
        Get the current value of a specific environmental condition.
        :param condition_name: The name of the environmental condition.
        :return: The value of the condition, or None if the condition is not found.
        """
        return self.environmental_conditions.get(condition_name)

    def remove_npc(self, npc_name):
        """
        Remove an NPC from the world state.
        :param npc_name: The name of the NPC to remove.
        """
        if npc_name in self.npc_positions:
            del self.npc_positions[npc_name]

    def clear_all(self):
        """
        Clear all NPC positions and environmental conditions.
        """
        self.npc_positions.clear()
        self.environmental_conditions.clear()

