# src/main.py

from src.ai.npc_mind import NPCMind
from src.environment import Environment  # Assuming there's an environment module
from src.npc import NPC  # Assuming there's an NPC module

def main():
    # Initialize environment and NPC
    environment = Environment()  # Create an instance of the game environment
    npc = NPC(name="Guardian", health=100)  # Create an NPC with initial attributes

    # Initialize NPC mind
    npc_mind = NPCMind()

    # Main game loop
    while True:
        # Update NPC mind with current NPC and environment
        npc_mind.update(npc, environment)

        # Simulate other game logic here
        # ...

        # Break condition for the loop (e.g., NPC dies or game ends)
        if npc.health <= 0:
            print(f"{npc.name} has perished.")
            break

if __name__ == "__main__":
    main()
