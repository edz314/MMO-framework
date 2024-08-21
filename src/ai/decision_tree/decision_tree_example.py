# Example of a Markov transition dictionary for an NPC
state_transitions = {
    "Aggressive": {"Aggressive": 0.7, "Defensive": 0.2, "Cautious": 0.1},
    "Defensive": {"Defensive": 0.5, "Aggressive": 0.3, "Flee": 0.2},
    "Cautious": {"Cautious": 0.6, "Aggressive": 0.3, "Neutral": 0.1},
    # Add more states and their transitions as needed
}
