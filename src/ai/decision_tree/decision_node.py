# src/ai/decision_tree/decision_node.py

from abc import ABC, abstractmethod
import random

class DecisionNode(ABC):
    @abstractmethod
    def evaluate(self, npc, environment):
        """
        Evaluate this node's condition.
        :param npc: The NPC being evaluated.
        :param environment: The environment or context in which the NPC operates.
        :return: The name of the state that the NPC should transition to.
        """
        pass


class DecisionLeaf(DecisionNode):
    def __init__(self, state_name):
        self.state_name = state_name

    def evaluate(self, npc, environment):
        """
        Return the state name that this leaf node represents.
        :param npc: The NPC being evaluated.
        :param environment: The environment or context in which the NPC operates.
        :return: The name of the state.
        """
        return self.state_name


class ConditionalDecisionNode(DecisionNode):
    def __init__(self, condition, true_branch, false_branch):
        """
        Initialize the decision node with a condition and branches.
        :param condition: A function that returns True or False based on npc and environment.
        :param true_branch: The node to evaluate if the condition is True.
        :param false_branch: The node to evaluate if the condition is False.
        """
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def evaluate(self, npc, environment):
        """
        Evaluate the condition and return the state from the appropriate branch.
        :param npc: The NPC being evaluated.
        :param environment: The environment or context in which the NPC operates.
        :return: The name of the state from the evaluated branch.
        """
        if self.condition(npc, environment):
            return self.true_branch.evaluate(npc, environment)
        else:
            return self.false_branch.evaluate(npc, environment)


class MarkovDecisionNode(DecisionNode):
    def __init__(self, state_transitions):
        """
        Initialize the Markov decision node with a state transition matrix.
        :param state_transitions: A dictionary where keys are state names and values are dictionaries
                                  with probabilities of transitioning to other states.
        """
        self.state_transitions = state_transitions

    def evaluate(self, npc, environment):
        """
        Evaluate and transition to the next state based on the Markov chain probabilities.
        :param npc: The NPC being evaluated.
        :param environment: The environment or context in which the NPC operates.
        :return: The name of the next state.
        """
        current_state = self.get_current_state_name(npc)
        transitions = self.state_transitions.get(current_state, {})

        if not transitions:
            return current_state  # No transition defined, stay in the current state

        next_state = self._weighted_random_choice(transitions)
        return next_state

    def get_current_state_name(self, npc):
        """Retrieve the current state name of the NPC."""
        return npc.get_current_state_name()

    def _weighted_random_choice(self, transitions):
        """Choose a next state based on weighted probabilities."""
        states = list(transitions.keys())
        probabilities = list(transitions.values())
        return random.choices(states, probabilities)[0]

