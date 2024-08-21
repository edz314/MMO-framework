# src/ai/actions/collect.py

from .action import Action

class CollectAction(Action):
    def __init__(self):
        super().__init__(name="Collect", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is collecting resources!")
        # Implement logic to collect resources or items in the environment
        item = environment.find_nearby_collectible(npc)
        if item:
            npc.collect_item(item)
