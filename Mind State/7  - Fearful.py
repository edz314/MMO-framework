# 7 - Fearful.py

from src.ai.fsm.fsm_state import FSMState

class FearfulState(FSMState):
    """
    Fearful State for NPCs. This state is used when the NPC is in a fearful mode,
    focusing on self-preservation by avoiding threats, hiding, or fleeing from danger.
    """

    def enter(self):
        """
        Called when the NPC enters the Fearful state. Sets up any necessary parameters.
        """
        print("NPC has entered Fearful State")
        # Example: Maximize fear level, reduce confidence
        self.fsm_controller.npc_data.fear_level = 100
        self.fsm_controller.npc_data.confidence_level = 10

    def execute(self):
        """
        Called on each game tick while in the Fearful state. Executes fearful behaviors.
        """
        print("NPC is acting fearfully, trying to avoid threats...")
        # Example: Check if there are nearby threats and decide to hide or flee
        if self.detect_threat():
            self.flee()
        else:
            self.hide()

    def exit(self):
        """
        Called when transitioning out of the Fearful state. Resets parameters to normal.
        """
        print("NPC is exiting Fearful State")
        # Example: Reset fear and confidence levels
        self.fsm_controller.npc_data.fear_level = 50
        self.fsm_controller.npc_data.confidence_level = 50

    def detect_threat(self):
        """
        Detect potential threats that cause fear in the NPC.
        :return: True if a threat is detected, False otherwise.
        """
        # Placeholder logic for detecting threats
        return True  # Replace with actual detection logic

    def flee(self):
        """
        Execute the logic to flee from the detected threat.
        """
        print("NPC is fleeing from the threat!")
        # Example: Transition to a Fleeing state or similar

    def hide(self):
        """
        Execute the logic to hide from potential threats.
        """
        print("NPC is hiding to avoid danger.")
        # Example: Transition to a Hiding state or stay in Fearful state
