# src/mind_state/1_aggressive.py

from src.ai.actions.attack import AttackAction
from src.ai.actions.roar import RoarAction
from src.ai.actions.plan_attack import PlanAttackAction
from src.ai.fsm.fsm_state import FSMState

class AggressiveState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the aggressive state
        self.actions = [AttackAction(), RoarAction(), PlanAttackAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Aggressive state.
        For example, check if the NPC has a target or enough health.
        """
        return npc.health > 20 and environment.has_visible_enemies(npc)

    def enter(self, npc):
        print(f"{npc.name} is entering Aggressive State.")
        # Additional setup when entering the aggressive state

    def execute(self, npc, environment):
        print(f"{npc.name} is in an aggressive state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        # Example state transition logic
        if npc.health < 20:
            self.fsm_controller.transition_to("Defensive")
