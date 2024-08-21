# 2 - Defensive.py

from src.ai.fsm.fsm_state import FSMState

class DefensiveState(FSMState):
    """
    Defensive State for NPCs. This state is used when the NPC is in a defensive mode,
    focusing on protecting itself and avoiding direct combat unless necessary.
    """

    def enter(self):
        """
        Called when the NPC enters the Defensive state. Sets up any necessary parameters.
        """
        print("NPC has entered Defensive State")
        # Example: Increase defense level, reduce aggression
        self.fsm_controller.npc_data.defense_level = 80
        self.fsm_controller.npc_data.aggression_level = 20

    def execute(self):
        """
        Called on each game tick while in the Defensive state. Executes defensive behaviors.
        """
        print("NPC is in defensive mode, avoiding conflict...")
        # Example: Check if an enemy is too close, then decide whether to flee or defend
        if self.is_enemy_nearby():
            self.defend()
        else:
            self.retreat()

    def exit(self):
        """
        Called when transitioning out of the Defensive state. Resets parameters to normal.
        """
        print("NPC is exiting Defensive State")
        # Example: Reset defense and aggression levels
        self.fsm_controller.npc_data.defense_level = 50
        self.fsm_controller.npc_data.aggression_level = 50

    def is_enemy_nearby(self):
        """
        Detect if an enemy is close enough to threaten the NPC.
        :return: True if an enemy is nearby, False otherwise.
        """
        # Placeholder logic for detecting nearby enemies
        return True  # Replace with actual detection logic

    def defend(self):
        """
        Perform defensive actions, such as blocking or countering attacks.
        """
        print("NPC is defending against an enemy!")

    def retreat(self):
        """
        Retreat from the enemy, moving to a safer location.
        """
        print("No immediate threat detected, NPC is retreating.")
        self.transition_to("Flee")  # Example transition to a Flee state
