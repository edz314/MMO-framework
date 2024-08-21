# 4 - Cautious.py

from src.ai.fsm.fsm_state import FSMState

class CautiousState(FSMState):
    """
    Cautious State for NPCs. This state is used when the NPC is in a cautious mode,
    focusing on careful movement, avoiding potential threats, and being alert to the surroundings.
    """

    def enter(self):
        """
        Called when the NPC enters the Cautious state. Sets up any necessary parameters.
        """
        print("NPC has entered Cautious State")
        # Example: Increase alertness level, reduce speed
        self.fsm_controller.npc_data.alertness_level = 90
        self.fsm_controller.npc_data.speed = 50  # Move slower when cautious

    def execute(self):
        """
        Called on each game tick while in the Cautious state. Executes cautious behaviors.
        """
        print("NPC is moving cautiously, scanning for threats...")
        # Example: Scan for nearby threats or traps
        if self.detect_threat():
            self.avoid()
        else:
            self.proceed_with_caution()

    def exit(self):
        """
        Called when transitioning out of the Cautious state. Resets parameters to normal.
        """
        print("NPC is exiting Cautious State")
        # Example: Reset alertness level and speed
        self.fsm_controller.npc_data.alertness_level = 50
        self.fsm_controller.npc_data.speed = 100

    def detect_threat(self):
        """
        Detect potential threats in the environment.
        :return: True if a threat is detected, False otherwise.
        """
        # Placeholder logic for detecting threats
        return True  # Replace with actual detection logic

    def avoid(self):
        """
        Take action to avoid detected threats.
        """
        print("NPC is avoiding a detected threat!")

    def proceed_with_caution(self):
        """
        Proceed with caution if no immediate threats are detected.
        """
        print("No immediate threat detected, NPC is proceeding cautiously.")
        # Example: Continue in the cautious state or transition to another cautious behavior
