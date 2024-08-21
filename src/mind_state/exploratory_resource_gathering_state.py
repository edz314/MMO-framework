# src/mind_state/exploratory_resource_gathering_state.py

from src.ai.actions.scout import ScoutAction
from src.ai.actions.collect import CollectAction
from src.ai.actions.investigate import InvestigateAction
from src.ai.fsm.fsm_state import FSMState

class ExploratoryResourceGatheringState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the exploratory-resource-gathering state
        self.actions = [ScoutAction(), CollectAction(), InvestigateAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Exploratory-ResourceGathering state.
        For example, the NPC might enter this state when exploring an area rich in resources.
        """
        return environment.has_resources_to_gather(npc) and environment.is_area_safe(npc)

    def enter(self, npc):
        print(f"{npc.name} is entering Exploratory-ResourceGathering State.")
        npc.set_exploration_gathering_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is exploring and gathering resources.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        if environment.detects_threat(npc):
            self.fsm_controller.transition_to("Cautious")
        elif npc.gathering_complete():
            self.fsm_controller.transition_to("Neutral")

    def exit(self, npc):
        print(f"{npc.name} is exiting Exploratory-ResourceGathering State.")
        npc.set_exploration_gathering_mode(False)
