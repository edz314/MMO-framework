# src/mind_state/2_defensive.py

from src.ai.actions.set_up_defenses import SetUpDefensesAction
from src.ai.actions.block import BlockAction
from src.ai.actions.retreat import RetreatAction
from src.ai.fsm.fsm_state import FSMState

class DefensiveState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the defensive state
        self.actions = [SetUpDefensesAction(), BlockAction(), RetreatAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Defensive state.
        For example, check if the NPC's health is low or if they are outnumbered.
        """
        return npc.health < 50 or environment.is_outnumbered(npc)

    def enter(self, npc):
        print(f"{npc.name} is entering Defensive State.")
        # Additional setup when entering the defensive state
        npc.increase_defense()

    def execute(self, npc, environment):
        print(f"{npc.name} is in a defensive state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if npc.health > 70 and environment.no_longer_outnumbered(npc):
            self.fsm_controller.transition_to("Aggressive")

    def exit(self, npc):
        print(f"{npc.name} is exiting Defensive State.")
        # Clean up or reset any modifications made during the defensive state
        npc.reset_defense()
