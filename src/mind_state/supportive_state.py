# src/mind_state/supportive_state.py

from src.ai.actions.call import CallAction
from src.ai.actions.cover import CoverAction
from src.ai.actions.coordinate_with_allies import CoordinateWithAlliesAction
from src.ai.fsm.fsm_state import FSMState

class SupportiveState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the supportive state
        self.actions = [CallAction(), CoverAction(), CoordinateWithAlliesAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Supportive state.
        For example, check if allies are in need of assistance or if the NPC is in a tactical role.
        """
        return environment.are_allies_in_need(npc) or npc.is_in_support_role()

    def enter(self, npc):
        print(f"{npc.name} is entering Supportive State.")
        # Additional setup when entering the supportive state
        npc.set_supportive_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is in a supportive state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if environment.threat_level_increases(npc):
            self.fsm_controller.transition_to("Defensive")

    def exit(self, npc):
        print(f"{npc.name} is exiting Supportive State.")
        # Clean up or reset any modifications made during the supportive state
        npc.set_supportive_mode(False)
