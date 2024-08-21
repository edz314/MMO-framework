# src/mind_state/5_neutral.py

from src.ai.actions.idle_wait import IdleWaitAction
from src.ai.actions.greet import GreetAction
from src.ai.actions.interact import InteractAction
from src.ai.fsm.fsm_state import FSMState

class NeutralState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the neutral state
        self.actions = [IdleWaitAction(), GreetAction(), InteractAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Neutral state.
        For example, check if the NPC is in a safe and non-hostile environment.
        """
        return environment.is_peaceful(npc)

    def enter(self, npc):
        print(f"{npc.name} is entering Neutral State.")
        # Additional setup when entering the neutral state
        npc.set_neutral_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is in a neutral state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if environment.detects_threat(npc):
            self.fsm_controller.transition_to("Cautious")

    def exit(self, npc):
        print(f"{npc.name} is exiting Neutral State.")
        # Clean up or reset any modifications made during the neutral state
        npc.set_neutral_mode(False)
