# src/ai/decision_tree/decision_tree_builder.py

from src.ai.decision_tree.decision_node import DecisionNode, DecisionLeaf, ConditionalDecisionNode, MarkovDecisionNode

class DecisionTreeBuilder:
    def __init__(self):
        self.root = None

    def build_tree(self):
        """
        Constructs the decision tree using a combination of decision nodes and leaf nodes.
        The tree can include conditional nodes and Markovian decision nodes.
        """
        # Example of combining conditional and Markov decision nodes:
        
        # Define the Markov transition probabilities
        markov_transitions = {
            "Aggressive": {"Aggressive": 0.7, "Defensive": 0.2, "Cautious": 0.1},
            "Defensive": {"Defensive": 0.5, "Aggressive": 0.3, "Flee": 0.2},
            "Cautious": {"Cautious": 0.6, "Aggressive": 0.3, "Neutral": 0.1},
        }
        
        markov_node = MarkovDecisionNode(state_transitions=markov_transitions)

        # Create conditional decision nodes
        health_low_node = ConditionalDecisionNode(
            condition=lambda npc, env: npc.health < 30,
            true_branch=DecisionLeaf("Defensive"),
            false_branch=markov_node
        )

        enemy_nearby_node = ConditionalDecisionNode(
            condition=lambda npc, env: env.is_enemy_nearby(npc),
            true_branch=DecisionLeaf("Alert"),
            false_branch=health_low_node
        )

        # Set the root of the tree
        self.root = enemy_nearby_node

    def get_decision_tree(self):
        """
        Returns the root of the constructed decision tree.
        """
        if not self.root:
            self.build_tree()
        return self.root

