# src/mind_state/4_cautious.py

from src.ai.actions.move_slowly import MoveSlowlyAction
from src.ai.actions.observe import ObserveAction
from src.ai.actions.hide import HideAction
from src.ai.fsm.fsm_state import FSMState

class CautiousState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the cautious state
        self.actions = [MoveSlowlyAction(), ObserveAction(), HideAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Cautious state.
        For example, check if the NPC is in a potentially dangerous area or if stealth is required.
        """
        return environment.is_potentially_dangerous(npc)

    def enter(self, npc):
        print(f"{npc.name} is entering Cautious State.")
        # Additional setup when entering the cautious state
        npc.set_caution_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is in a cautious state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if npc.detects_immediate_threat(environment):
            self.fsm_controller.transition_to("Defensive")
        elif environment.is_safe_area(npc):
            self.fsm_controller.transition_to("Exploratory")

    def exit(self, npc):
        print(f"{npc.name} is exiting Cautious State.")
        # Clean up or reset any modifications made during the cautious state
        npc.set_caution_mode(False)
