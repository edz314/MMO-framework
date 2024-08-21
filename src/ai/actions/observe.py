# src/ai/actions/observe.py

from .action import Action

class ObserveAction(Action):
    def __init__(self):
        super().__init__(name="Observe", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is observing the surroundings!")
        # Implement logic for the NPC to observe and gather information about the environment
        observations = environment.observe_area(npc.position)
        npc.record_observations(observations)
