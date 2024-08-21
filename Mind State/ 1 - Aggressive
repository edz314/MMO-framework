# 1 - Aggressive.py

from src.ai.fsm.fsm_state import FSMState

class AggressiveState(FSMState):
    """
    Aggressive State for NPCs. This state is used when the NPC is in an aggressive mode,
    actively seeking to engage and attack enemies.
    """

    def enter(self):
        """
        Called when the NPC enters the Aggressive state. Sets up any necessary parameters.
        """
        print("NPC has entered Aggressive State")
        # Example: Set aggression level to maximum
        self.fsm_controller.npc_data.aggression_level = 100

    def execute(self):
        """
        Called on each game tick while in the Aggressive state. Executes aggressive behaviors.
        """
        print("NPC is aggressively seeking targets...")
        # Example: Search for nearby enemies
        if self.detect_enemies():
            self.attack()
        else:
            self.patrol()

    def exit(self):
        """
        Called when transitioning out of the Aggressive state. Cleans up or resets parameters.
        """
        print("NPC is exiting Aggressive State")
        # Example: Lower aggression level
        self.fsm_controller.npc_data.aggression_level = 50

    def detect_enemies(self):
        """
        Detect nearby enemies.
        :return: True if enemies are detected, False otherwise.
        """
        # This function would contain logic to detect enemies within range.
        return True  # Placeholder for actual detection logic

    def attack(self):
        """
        Perform an attack on the detected enemy.
        """
        print("NPC is attacking the enemy!")

    def patrol(self):
        """
        Patrol the area if no enemies are detected.
        """
        print("No enemies detected, NPC is patrolling.")
        self.transition_to("Patrol")  # Example transition
