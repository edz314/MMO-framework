**Project Architecture**

**Overview of the System Architecture**
The MMO-framework is designed to provide a modular and scalable structure for managing NPC behavior in a game environment. The architecture is centered around the concepts of Finite State Machines (FSM), Decision Trees, and NPC Minds, allowing for flexible and dynamic control of NPCs based on environmental inputs and internal states.

Key Components and Their Interactions

**1. NPCMind**
Description: Centralizes the behavior and state management of an NPC.
Interaction: Integrates with the FSM to manage state transitions based on decisions made by the Decision Tree.

**3. FSM (Finite State Machine)**
Description: Manages the states that an NPC can be in, such as Aggressive, Defensive, etc.
Interaction: Each state in the FSM is associated with specific behaviors and can transition based on conditions or triggers from the environment.

**5. Decision Tree**
Description: Evaluates conditions and determines the appropriate state for an NPC to transition into.
Interaction: Feeds into the FSM to dictate state transitions based on dynamic game conditions.

**7. NPCData**
Description: Holds all relevant data for an NPC, including health, inventory, and current state.
Interaction: Used by both FSM and Decision Tree to determine behavior and state transitions.

**9. WorldState**
Description: Manages the global state of the game world, including environmental conditions and NPC positions.
Interaction: Provides context to NPCs for making decisions and changing states.

**Flow Diagrams / Sequence Diagrams**

**State Transition Example:**
Here is a worked state transition example as mermaid script

https://github.com/edz314/MMO-framework/blob/master/Docs/state_file.mermaid


**Data Flow Example:**
Here is a worked data flow example as mermaid script

https://github.com/edz314/MMO-framework/blob/master/Docs/data_flow.mermaid

**Explanation of FSM, Decision Tree, and NPC Mind Logic**

**FSM (Finite State Machine)**
The FSM controls the active state of an NPC. States represent different behaviors (e.g., Aggressive, Defensive), and the FSM transitions between these states based on triggers or conditions provided by the Decision Tree and the environment.

**Decision Tree**
The Decision Tree evaluates game conditions, such as proximity to enemies or health levels, and determines the most appropriate state for the NPC to enter. The output of the Decision Tree informs the FSM on how to transition between states.

**NPC Mind Logic**
The NPCMind orchestrates the overall decision-making process. It leverages the Decision Tree to assess conditions and instructs the FSM to execute appropriate behavior. The NPCMind also interacts with NPCData to track the NPC's current state, inventory, and other attributes.

**Data Flow and Communication Between Modules**

NPCMind acts as the central controller, receiving inputs from the WorldState and Decision Tree.

The FSM manages state transitions based on instructions from the Decision Tree.

NPCData stores the current state and inventory, which are crucial for decision-making.

**High level architecture**

This is the high level architecture expressed as a mermaid script at the L1 component level

https://github.com/edz314/MMO-framework/blob/master/Docs/high_level_architecture.mermaid

**Low Level Architecture**

This is the hilow level architecture expressed as a mermaid script at the L3 function level

https://github.com/edz314/MMO-framework/blob/master/Docs/low_level_architecture.mermaid




WorldState provides environmental context that influences NPC behavior.

This modular design allows for flexibility and extensibility, making it easy to introduce new states, actions, and decision logic as needed.
