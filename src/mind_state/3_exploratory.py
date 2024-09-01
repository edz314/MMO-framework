# src/mind_state/3_exploratory.py

from src.ai.actions.scout import ScoutAction
from src.ai.actions.investigate import InvestigateAction
from src.ai.actions.observe import ObserveAction
from src.ai.fsm.fsm_state import FSMState

class ExploratoryState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the exploratory state
        self.actions = [ScoutAction(), InvestigateAction(), ObserveAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Exploratory state.
        For example, check if the area is safe or if there is something of interest to explore.
        """
        return environment.is_area_safe(npc) and environment.has_points_of_interest(npc)

    def enter(self, npc):
        print(f"{npc.name} is entering Exploratory State.")
        # Additional setup when entering the exploratory state
        npc.set_exploration_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is in an exploratory state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if environment.detects_threat(npc):
            self.fsm_controller.transition_to("Defensive")

    def exit(self, npc):
        print(f"{npc.name} is exiting Exploratory State.")
        # Clean up or reset any modifications made during the exploratory state
        npc.set_exploration_mode(False)


