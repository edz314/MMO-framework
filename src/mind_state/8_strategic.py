# src/mind_state/8_strategic.py

from src.ai.actions.plan_attack import PlanAttackAction
from src.ai.actions.coordinate_with_allies import CoordinateWithAlliesAction
from src.ai.actions.set_up_defenses import SetUpDefensesAction
from src.ai.fsm.fsm_state import FSMState

class StrategicState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the strategic state
        self.actions = [PlanAttackAction(), CoordinateWithAlliesAction(), SetUpDefensesAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Strategic state.
        For example, check if the NPC has the resources and opportunity to plan and execute strategies.
        """
        return npc.has_resources() and environment.is_suitable_for_planning(npc)

    def enter(self, npc):
        print(f"{npc.name} is entering Strategic State.")
        # Additional setup when entering the strategic state
        npc.set_strategic_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is in a strategic state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if environment.detects_immediate_threat(npc):
            self.fsm_controller.transition_to("Defensive")
        elif npc.objectives_met():
            self.fsm_controller.transition_to("Neutral")

    def exit(self, npc):
        print(f"{npc.name} is exiting Strategic State.")
        # Clean up or reset any modifications made during the strategic state
        npc.set_strategic_mode(False)
