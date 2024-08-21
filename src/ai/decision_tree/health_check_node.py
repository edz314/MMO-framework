# src/ai/decision_tree/health_check_node.py

from src.ai.decision_tree.decision_node import DecisionNode, DecisionLeaf, ConditionalDecisionNode

class HealthCheckNode(ConditionalDecisionNode):
    def __init__(self, low_health_threshold=30):
        """
        Initialize the HealthCheckNode with a health threshold.
        :param low_health_threshold: The health value below which the NPC is considered to have low health.
        """
        self.low_health_threshold = low_health_threshold

        # Define the branches
        true_branch = DecisionLeaf("Defensive")
        false_branch = DecisionLeaf("Aggressive")

        # Initialize the base ConditionalDecisionNode with the health condition
        super().__init__(
            condition=self.is_health_low,
            true_branch=true_branch,
            false_branch=false_branch
        )

    def is_health_low(self, npc, environment):
        """
        Condition to check if the NPC's health is below the low health threshold.
        :param npc: The NPC being evaluated.
        :param environment: The environment or context in which the NPC operates.
        :return: True if the NPC's health is low, otherwise False.
        """
        return npc.health < self.low_health_threshold

