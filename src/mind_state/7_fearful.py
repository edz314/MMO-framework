# src/mind_state/7_fearful.py

from src.ai.actions.flee import FleeAction
from src.ai.actions.hide import HideAction
from src.ai.actions.beg_for_mercy import BegForMercyAction
from src.ai.fsm.fsm_state import FSMState

class FearfulState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the fearful state
        self.actions = [FleeAction(), HideAction(), BegForMercyAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Fearful state.
        For example, check if the NPC is low on health or significantly outmatched.
        """
        return npc.health < 30 or environment.is_overwhelming(npc)

    def enter(self, npc):
        print(f"{npc.name} is entering Fearful State.")
        # Additional setup when entering the fearful state
        npc.set_fearful_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is in a fearful state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if npc.finds_safe_spot(environment):
            self.fsm_controller.transition_to("Neutral")

    def exit(self, npc):
        print(f"{npc.name} is exiting Fearful State.")
        # Clean up or reset any modifications made during the fearful state
        npc.set_fearful_mode(False)
