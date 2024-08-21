# src/mind_state/defensive_strategic_state.py

from src.ai.actions.set_up_defenses import SetUpDefensesAction
from src.ai.actions.plan_attack import PlanAttackAction
from src.ai.actions.coordinate_with_allies import CoordinateWithAlliesAction
from src.ai.fsm.fsm_state import FSMState

class DefensiveStrategicState(FSMState):
    def __init__(self, fsm_controller):
        super().__init__(fsm_controller)
        # Assign relevant actions for the defensive-strategic state
        self.actions = [SetUpDefensesAction(), PlanAttackAction(), CoordinateWithAlliesAction()]

    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter the Defensive-Strategic state.
        Enter if the NPC needs to balance defense with strategic planning.
        """
        return npc.health < 50 and npc.has_allies_nearby()

    def enter(self, npc):
        print(f"{npc.name} is entering Defensive-Strategic State.")
        npc.set_defensive_strategic_mode(True)

    def execute(self, npc, environment):
        print(f"{npc.name} is in a defensive-strategic state.")
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

        if npc.health > 70:
            self.fsm_controller.transition_to("Aggressive")
        elif npc.objectives_met():
            self.fsm_controller.transition_to("Neutral")

    def exit(self, npc):
        print(f"{npc.name} is exiting Defensive-Strategic State.")
        npc.set_defensive_strategic_mode(False)
