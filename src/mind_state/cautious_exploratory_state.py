# src/mind_state/cautious_exploratory_state.py

from src.ai.actions.move_slowly import MoveSlowlyAction
from src.ai.actions.observe import ObserveAction
from src.ai.actions.scout import ScoutAction
from src.ai.fsm.fsm_state import FSMState

class CautiousExploratoryState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the cautious-exploratory state
        self.actions = [MoveSlowlyAction(), ObserveAction(), ScoutAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Cautious-Exploratory state.
        For example, the NPC might enter this state when exploring an area with known dangers.
        """
        return environment.is_potentially_dangerous(npc) and environment.has_points_of_interest(npc)

    def enter(self, npc):
        print(f"{npc.name} is entering Cautious-Exploratory State.")
        # Additional setup when entering the cautious-exploratory state
        npc.set_cautious_exploration_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is cautiously exploring.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if environment.detects_immediate_threat(npc):
            self.fsm_controller.transition_to("Defensive")
        elif environment.is_safe_area(npc):
            self.fsm_controller.transition_to("Exploratory")

    def exit(self, npc):
        print(f"{npc.name} is exiting Cautious-Exploratory State.")
        # Clean up or reset any modifications made during the cautious-exploratory state
        npc.set_cautious_exploration_mode(False)
