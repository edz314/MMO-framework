# 6 - Alert.py

from src.ai.fsm.fsm_state import FSMState

class AlertState(FSMState):
    """
    Alert State for NPCs. This state is used when the NPC is in an alert mode,
    focusing on heightened awareness of the surroundings and ready to respond to any threats.
    """

    def enter(self):
        """
        Called when the NPC enters the Alert state. Sets up any necessary parameters.
        """
        print("NPC has entered Alert State")
        # Example: Maximize alertness and increase perception
        self.fsm_controller.npc_data.alertness_level = 100
        self.fsm_controller.npc_data.perception_range = 150  # Increase perception range

    def execute(self):
        """
        Called on each game tick while in the Alert state. Executes alert behaviors.
        """
        print("NPC is highly alert, scanning for threats...")
        # Example: Check for threats in the environment and prepare to react
        if self.detect_threat():
            self.prepare_for_action()
        else:
            self.maintain_alertness()

    def exit(self):
        """
        Called when transitioning out of the Alert state. Resets parameters to normal.
        """
        print("NPC is exiting Alert State")
        # Example: Reset alertness and perception range
        self.fsm_controller.npc_data.alertness_level = 50
        self.fsm_controller.npc_data.perception_range = 100

    def detect_threat(self):
        """
        Detect potential threats in the environment.
        :return: True if a threat is detected, False otherwise.
        """
        # Placeholder logic for detecting threats
        return True  # Replace with actual detection logic

    def prepare_for_action(self):
        """
        Prepare to take action against a detected threat.
        """
        print("NPC has detected a threat and is preparing to respond!")
        self.transition_to("Aggressive")  # Example transition to Aggressive state

    def maintain_alertness(self):
        """
        Maintain high alertness if no immediate threats are detected.
        """
        print("No immediate threat detected, NPC remains on high alert.")
