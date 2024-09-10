# src/data/npc_data.py

class NPCData:
    def __init__(self, name, health=100, inventory=None):
        """
        Initialize the NPCData class.
        :param name: The name of the NPC.
        :param health: The health of the NPC.
        :param inventory: The inventory of the NPC, defaulting to an empty list.
        """

        self.name = name
        self.health = health
        self.inventory = inventory or []
        self.current_state_name = "Neutral"
        self.position = (0, 0)  # Default position, can be updated by game logic

    def update_health(self, amount):
        """

        Update the health of the NPC.
        :param amount: The amount to modify health by (can be positive or negative).
        """

        self.health += amount
        if self.health < 0:
            self.health = 0
        elif self.health > 100:
            self.health = 100

    def get_current_state_name(self):
        """
        Return the current state name of the NPC.
        :return: The name of the current state.
        """
        return self.current_state_name

    def set_current_state_name(self, state_name):
        """
        Set the current state name of the NPC.
        :param state_name: The name of the new state.
        """

        self.current_state_name = state_name

    def add_to_inventory(self, item):
        """

        Add an item to the NPC's inventory.
        :param item: The item to add to the inventory.
        """
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        """

        Remove an item from the NPC's inventory.
        :param item: The item to remove from the inventory.
        """
        if item in self.inventory:
            self.inventory.remove(item)

    def has_item(self, item):
        """
        Check if the NPC has a specific item in their inventory.
        :param item: The item to check for.
        :return: True if the item is in the inventory, False otherwise.
        """

        return item in self.inventory

    def is_alive(self):
        """

        Check if the NPC is alive.
        :return: True if health is greater than 0, False otherwise.
        """

        return self.health > 0


