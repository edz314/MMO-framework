# main.py

from src.ai.fsm.fsm_controller import FSMController
from src.ai.decision_tree.decision_tree_builder import DecisionTreeBuilder
from src.ai.npc_mind import NPCMind
from src.data.npc_data import NPCData
from src.data.world_state import WorldState

def main():
    # Initialize NPC data and world state
    npc_data = NPCData(health=100, aggression_level=50)
    world_state = WorldState(player_position=(10, 20), enemy_position=(15, 25))
    
    # Create and configure the NPC mind
    npc_mind = NPCMind(npc_data=npc_data, world_state=world_state)
    
    # Setup the FSM for the NPC
    fsm_controller = FSMController()
    fsm_controller.add_state("Idle", npc_mind.idle_state)
    fsm_controller.add_state("Patrol", npc_mind.patrol_state)
    fsm_controller.add_state("Attack", npc_mind.attack_state)
    
    # Create a decision tree for the NPC
    decision_tree_builder = DecisionTreeBuilder()
    decision_tree = decision_tree_builder.build_tree()
    
    # Main loop simulation
    while True:
        # Update world state (mocked here)
        world_state.update(player_position=(12, 22))
        
        # Run decision tree to determine the next state
        next_state = decision_tree.evaluate(npc_data, world_state)
        fsm_controller.transition_to(next_state)
        
        # Execute the current state logic
        fsm_controller.execute_state()
        
        # Simulate a game tick (or break out of the loop)
        break  # Remove or replace with actual game loop condition

if __name__ == "__main__":
    main()

