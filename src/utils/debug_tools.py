# src/utils/debug_tools.py

def log_npc_state(npc):
    """
    Log the current state and relevant details of the NPC for debugging purposes.
    :param npc: The NPC whose state will be logged.
    """
    print(f"NPC Name: {npc.name}")
    print(f"Health: {npc.health}")
    print(f"Current State: {npc.get_current_state_name()}")
    print(f"Inventory: {npc.inventory}")
    print(f"Position: {npc.position}")
    print("-" * 20)

def log_world_state(world_state):
    """
    Log the current state of the game world for debugging purposes.
    :param world_state: The WorldState instance containing the game's state.
    """
    print("World State:")
    print("NPC Positions:")
    for npc_name, position in world_state.npc_positions.items():
        print(f"  {npc_name}: {position}")
    print("Environmental Conditions:")
    for condition_name, value in world_state.environmental_conditions.items():
        print(f"  {condition_name}: {value}")
    print("-" * 20)

def log_message(message, level="INFO"):
    """
    Log a custom message with a specified level.
    :param message: The message to log.
    :param level: The log level (e.g., INFO, DEBUG, WARNING, ERROR).
    """
    print(f"[{level}] {message}")

def log_decision_tree_evaluation(decision_node, npc, environment):
    """
    Log the decision-making process within the decision tree.
    :param decision_node: The current node being evaluated in the decision tree.
    :param npc: The NPC involved in the decision-making.
    :param environment: The environment context in which the decision is being made.
    """
    state = decision_node.evaluate(npc, environment)
    print(f"Evaluating Decision Node: {decision_node.__class__.__name__}")
    print(f"Resulting State: {state}")
    print("-" * 20)

