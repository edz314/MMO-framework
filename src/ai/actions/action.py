# src/ai/actions/action.py

class Action:
    def __init__(self, name, prerequisites=None, dependencies=None):
        """
        Initialize the Action class.

        :param name: Name of the action.
        :param prerequisites: List of prerequisites needed to perform the action.
        :param dependencies: List of dependencies that need to be satisfied.
        """
        self.name = name
        self.prerequisites = prerequisites or []
        self.dependencies = dependencies or []

    def can_execute(self, npc):
        """
        Check if the action can be executed based on the NPC's state.

        :param npc: The NPC attempting to perform the action.
        :return: True if the action can be executed, False otherwise.
        """
        return all(item in npc.inventory for item in self.prerequisites)

    def execute(self, npc, environment):
        """
        Execute the action.

        :param npc: The NPC performing the action.
        :param environment: The environment or context in which the action is being performed.
        """
        pass  # To be overridden by specific actions
