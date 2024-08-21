# 3 - Exploratory.py

from src.ai.fsm.fsm_state import FSMState

class ExploratoryState(FSMState):
    """
    Exploratory State for NPCs. This state is used when the NPC is in an exploratory mode,
    focused on discovering new areas, gathering information, or interacting with the environment.
    """

    def enter(self):
        """
        Called when the NPC enters the Exploratory state. Sets up any necessary parameters.
        """
        print("NPC has entered Exploratory State")
        # Example: Increase curiosity level, reduce aggression
        self.fsm_controller.npc_data.curiosity_level = 80
        self.fsm_controller.npc_data.aggression_level = 10

    def execute(self):
        """
        Called on each game tick while in the Exploratory state. Executes exploratory behaviors.
        """
        print("NPC is exploring the surroundings...")
        # Example: Search for points of interest, interact with objects, or gather resources
        if self.detect_point_of_interest():
            self.investigate()
        else:
            self.wander()

    def exit(self):
        """
        Called when transitioning out of the Exploratory state. Resets parameters to normal.
        """
        print("NPC is exiting Exploratory State")
        # Example: Reset curiosity level
        self.fsm_controller.npc_data.curiosity_level = 50

    def detect_point_of_interest(self):
        """
        Detect points of interest in the environment.
        :return: True if a point of interest is detected, False otherwise.
        """
        # Placeholder logic for detecting points of interest
        return True  # Replace with actual detection logic

    def investigate(self):
        """
        Investigate the detected point of interest.
        """
        print("NPC is investigating a point of interest!")

    def wander(self):
        """
        Wander around if no specific point of interest is detected.
        """
        print("No point of interest detected, NPC is wandering.")
        # Example: Stay in the exploratory state or transition to another exploratory behavior
