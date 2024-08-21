# src/ai/npc_mind.py

from src.ai.fsm.fsm_controller import FSMController
from src.ai.decision_tree.decision_tree_builder import DecisionTreeBuilder
from src.mind_state.aggressive_state import AggressiveState
from src.mind_state.defensive_state import DefensiveState
from src.mind_state.cautious_state import CautiousState
from src.mind_state.exploratory_state import ExploratoryState
from src.mind_state.neutral_state import NeutralState
from src.mind_state.alert_state import AlertState
from src.mind_state.strategic_state import StrategicState
from src.mind_state.fearful_state import FearfulState

class NPCMind:
    def __init__(self):
        # Initialize the FSM and Decision Tree
        self.fsm = FSMController()
        self.decision_tree_builder = DecisionTreeBuilder()

        # Build the decision tree
        self.decision_tree = self.decision_tree_builder.get_decision_tree()

        # Add states to the FSM
        self.fsm.add_state("Aggressive", AggressiveState(self.fsm))
        self.fsm.add_state("Defensive", DefensiveState(self.fsm))
        self.fsm.add_state("Cautious", CautiousState(self.fsm))
        self.fsm.add_state("Exploratory", ExploratoryState(self.fsm))
        self.fsm.add_state("Neutral", NeutralState(self.fsm))
        self.fsm.add_state("Alert", AlertState(self.fsm))
        self.fsm.add_state("Strategic", StrategicState(self.fsm))
        self.fsm.add_state("Fearful", FearfulState(self.fsm))

        # Start with a neutral state
        self.fsm.transition_to("Neutral")

    def update(self, npc, environment):
        """
        Update the NPC's mind, deciding on the next state and executing the current state.
        :param npc: The NPC being controlled.
        :param environment: The environment in which the NPC operates.
        """
        # Use the decision tree to determine the next state
        next_state = self.decision_tree.evaluate(npc, environment)

        # Transition to the decided state
        self.fsm.transition_to(next_state)

        # Execute the current state
        self.fsm.execute_state(npc, environment)

