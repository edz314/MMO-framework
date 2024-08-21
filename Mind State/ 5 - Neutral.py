# 5 - Neutral.py

from src.ai.fsm.fsm_state import FSMState

class NeutralState(FSMState):
    """
    Neutral State for NPCs. This state is used when the NPC is in a neutral mode,
    neither aggressive nor defensive, focusing on regular behaviors without reacting to external stimuli.
    """

    def enter(self):
        """
        Called when the NPC enters the Neutral state. Sets up any necessary parameters.
        """
        print("NPC has entered Neutral State")
        # Example: Set aggression and defense to balanced levels
        self.fsm_controller.npc_data.aggression_level = 50
        self.fsm_controller.npc_data.defense_level = 50

    def execute(self):
        """
        Called on each game tick while in the Neutral state. Executes neutral behaviors.
        """
        print("NPC is in a neutral state, behaving normally...")
        # Example: Perform routine tasks like walking or interacting with the environment
        self.perform_routine_tasks()

    def exit(self):
        """
        Called when transitioning out of the Neutral state. Resets parameters if necessary.
        """
        print("NPC is exiting Neutral State")

    def perform_routine_tasks(self):
        """
        Perform routine, non-reactive tasks.
        """
        print("NPC is performing routine tasks without any particular bias.")
        # Example: Continue in the neutral state or transition based on new conditions
