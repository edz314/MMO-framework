# src/mind_state/resource_gathering_state.py

from src.ai.actions.collect import CollectAction
from src.ai.actions.interact import InteractAction
from src.ai.actions.waypoints import WaypointsAction
from src.ai.fsm.fsm_state import FSMState

class ResourceGatheringState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the resource-gathering state
        self.actions = [CollectAction(), InteractAction(), WaypointsAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Resource Gathering state.
        For example, check if there are resources available or if the NPC is tasked with gathering.
        """
        return environment.has_resources_to_gather(npc) or npc.has_gathering_task()

    def enter(self, npc):
        print(f"{npc.name} is entering Resource Gathering State.")
        # Additional setup when entering the resource-gathering state
        npc.prepare_for_gathering()

    def execute(self, npc, environment):
        print(f"{npc.name} is in a resource-gathering state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if npc.gathering_complete():
            self.fsm_controller.transition_to("Neutral")

    def exit(self, npc):
        print(f"{npc.name} is exiting Resource Gathering State.")
        # Clean up or reset any modifications made during the resource-gathering state
        npc.reset_gathering_mode()
