# src/ai/npc_mind.py

import os
import importlib
from src.ai.fsm.fsm_controller import FSMController
from src.ai.decision_tree.decision_tree_builder import DecisionTreeBuilder

class NPCMind:
    def __init__(self):
        # Initialize the FSM
        self.fsm = FSMController()
        
        # Initialize and build the decision tree
        self.decision_tree = self._initialize_decision_tree()

        # Dynamically load and add all mind states to the FSM
        self._initialize_states()

        # Start in a neutral state
        self.fsm.transition_to("Neutral")

    def _initialize_decision_tree(self):
        """Build and return the decision tree."""
        decision_tree_builder = DecisionTreeBuilder()
        decision_tree_builder.build_tree()
        return decision_tree_builder.get_decision_tree()

    def _initialize_states(self):
        """Dynamically import and add all mind states to the FSM."""
        mind_state_dir = os.path.join(os.path.dirname(__file__), '..', 'mind_state')
        for filename in os.listdir(mind_state_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = f"src.mind_state.{filename[:-3]}"
                module = importlib.import_module(module_name)
                class_name = ''.join([word.capitalize() for word in filename[:-3].split('_')])
                state_class = getattr(module, class_name)
                self.fsm.add_state(class_name, state_class(self.fsm))

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
