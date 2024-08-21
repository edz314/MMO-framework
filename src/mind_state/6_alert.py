# src/mind_state/6_alert.py

from src.ai.actions.scan_area import ScanAreaAction
from src.ai.actions.observe import ObserveAction
from src.ai.actions.alert_allies import AlertAlliesAction
from src.ai.fsm.fsm_state import FSMState

class AlertState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the alert state
        self.actions = [ScanAreaAction(), ObserveAction(), AlertAlliesAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Alert state.
        For example, check if there are signs of danger or if the NPC needs to stay vigilant.
        """
        return environment.has_potential_threats(npc)

    def enter(self, npc):
        print(f"{npc.name} is entering Alert State.")
        # Additional setup when entering the alert state
        npc.set_alert_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is in an alert state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if environment.detects_immediate_threat(npc):
            self.fsm_controller.transition_to("Defensive")
        elif environment.is_safe_area(npc):
            self.fsm_controller.transition_to("Neutral")

    def exit(self, npc):
        print(f"{npc.name} is exiting Alert State.")
        # Clean up or reset any modifications made during the alert state
        npc.set_alert_mode(False)
