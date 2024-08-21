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
