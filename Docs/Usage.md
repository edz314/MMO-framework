Usage Guide
This document provides detailed instructions on how to use the MMO-framework project, including how to create and manage NPCs, extend the system, configure the environment, and run the project.

**1. Creating and Managing NPCs**
**Creating an NPC**
To create an NPC, you will need to define its initial attributes, including its name, health, inventory, and mind type. This is typically done using the NPCData class.

**#example code#**
from src.data.npc_data import NPCData

npc_data = NPCData(
    name="Guardian",
    health=100,
    inventory=["sword", "shield"],
    current_mind_type="Warrior"
)

**Managing NPCs**
NPCs are managed through the NPCMind class, which integrates FSM logic and decision trees to control NPC behavior.

**#example code#**
from src.ai.npc_mind import NPCMind

npc_mind = NPCMind(npc_data)

# To update NPC behavior based on the environment:
npc_mind.update(environment)


**Switching Mind Types**
You can switch an NPC’s mind type if they possess the required items for the new role.

**#example code#**
npc_mind.fsm.switch_mind_type("Archer")

**2. Extending the System**

**Adding New States**
To add a new state to the FSM, create a new state class in the mind_state directory. This class should inherit from the FSMState class.

# src/mind_state/aggressive_state.py

from src.ai.fsm.fsm_state import FSMState

class AggressiveState(FSMState):
    def enter(self, npc):
        print(f"{npc.name} is now aggressive.")

    def execute(self, npc, environment):
        # Define aggressive behavior
        pass

**Adding New Actions**
Actions are defined in the Actions directory. You can add a new action by creating a Python file that defines the action’s logic.

# src/actions/attack.py

class AttackAction:
    def execute(self, npc, target):
        # Define attack logic
        pass

**Integrating New States and Actions**
Once the new state or action is defined, integrate it into the FSMController or DecisionTreeBuilder.

# In FSMController
self.fsm.add_state("Aggressive", AggressiveState(self.fsm))

# In DecisionTreeBuilder
self.root = ConditionalDecisionNode(
    condition=lambda npc, env: npc.health < 50,
    true_branch=DecisionLeaf("Defensive"),
    false_branch=DecisionLeaf("Aggressive")
)


**3. Configuring and Running the Project**

**Environment Setup**
Set up the project environment by installing the required dependencies. Ensure you have Python installed, then run:

pip install -r requirements.txt
Running the Project
You can run the project’s main script, which will initialize the game environment and start NPC interactions.

bash
Copy code
python src/main.py

**Example Configuration**
Here’s an example configuration for an NPC named "Archer 1" with a specific mind type and starting inventory:

npc_data = NPCData(
    name="Archer 1",
    health=80,
    inventory=["bow", "arrows"],
    current_mind_type="Archer"
)

npc_mind = NPCMind(npc_data)
npc_mind.update(environment)


**4. Environment Setup and Configuration**

**Setting Up the Environment Module**

The environment provides context for NPCs, such as weather conditions and the presence of enemies.

# src/environment.py

class Environment:
    def __init__(self):
        self.weather = "sunny"
        self.time_of_day = "morning"

    def is_enemy_nearby(self, npc):
        return True  # or some logic to determine proximity


**Configuring Environment Parameters**

You can configure various parameters in the environment to simulate different scenarios:

environment = Environment()
environment.weather = "rainy"
environment.time_of_day = "night"

**Running with Custom Configurations**

Run the project with custom NPCs and environment settings:

from src.data.npc_data import NPCData
from src.ai.npc_mind import NPCMind
from src.environment import Environment

npc_data = NPCData(name="Guardian", health=100, inventory=["sword", "shield"], current_mind_type="Warrior")
npc_mind = NPCMind(npc_data)

environment = Environment()
npc_mind.update(environment)
