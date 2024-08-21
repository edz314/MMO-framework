# src/ai/actions/interact.py

from .action import Action

class InteractAction(Action):
    def __init__(self):
        super().__init__(name="Interact", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is interacting with the environment!")
        # Implement logic for the NPC to interact with objects in the environment
        interactable_object = environment.find_nearby_interactable(npc)
        if interactable_object:
            npc.interact_with(interactable_object)
