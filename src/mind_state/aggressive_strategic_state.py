# src/mind_state/aggressive_strategic_state.py

from src.ai.actions.attack import AttackAction
from src.ai.actions.plan_attack import PlanAttackAction
from src.ai.actions.coordinate_with_allies import CoordinateWithAlliesAction
from src.ai.fsm.fsm_state import FSMState

class AggressiveStrategicState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the aggressive-strategic state
        self.actions = [AttackAction(), PlanAttackAction(), CoordinateWithAlliesAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Aggressive-Strategic state.
        For example, enter this state if the NPC needs to balance direct combat with strategic planning.
        """
        return npc.is_in_combat() and npc.has_allies_nearby()

    def enter(self, npc):
        print(f"{npc.name} is entering Aggressive-Strategic State.")
        # Additional setup when entering the aggressive-strategic state
        npc.set_aggressive_strategic_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is in an aggressive-strategic state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if npc.health < 30:
            self.fsm_controller.transition_to("Defensive")
        elif npc.objectives_met():
            self.fsm_controller.transition_to("Neutral")

    def exit(self, npc):
        print(f"{npc.name} is exiting Aggressive-Strategic State.")
        # Clean up or reset any modifications made during the aggressive-strategic state
        npc.set_aggressive_strategic_mode(False)
