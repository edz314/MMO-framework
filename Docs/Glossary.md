**Glossary**

This glossary provides definitions for key terms and concepts used throughout the MMO-framework project.

**Key Terms**

**FSM (Finite State Machine)**
A computational model used to design NPC behaviors where the system can be in one of a finite number of states. Transitions between states occur based on triggers or conditions.

**Decision Tree**
A tree-like model used for decision-making. Each node represents a condition or decision, leading to different branches and ultimately determining the state or action an NPC should take.

**NPC (Non-Player Character)**
A character in the game that is not controlled by a player but by the game’s AI. NPCs can interact with players, the environment, and other NPCs.

**Mind State**
A specific behavioral mode or role that an NPC can assume, such as Aggressive, Defensive, or Exploratory. Each mind state dictates the NPC's actions and reactions based on the current context.

**Action**
A specific behavior or task that an NPC can perform, such as Attack, Patrol, or Flee. Actions are typically tied to an NPC’s current mind state.

**NPCMind**
The central controller for an NPC’s behavior, managing the FSM and decision-making processes, and determining how the NPC interacts with the game environment.

**WorldState**
The current state of the game world, including environmental conditions, NPC positions, and other global variables that influence NPC behavior.

**NPCData**
A data structure that holds all relevant attributes and information for an NPC, such as health, inventory, and current state.

**Environment**
The simulated game world in which NPCs operate, providing context and conditions that influence NPC behavior.

**State Transition**
The process of moving from one state to another within an FSM, triggered by specific conditions or decisions made by the Decision Tree.

**Inventory**
A collection of items that an NPC possesses, which may influence their ability to perform certain actions or switch mind states.

**Module**
A self-contained unit of code that encapsulates specific functionality, such as FSM, Decision Tree, or WorldState.

**Mock Environment**
A simplified or simulated environment used in testing to mimic the real game world, allowing for controlled testing of NPC behaviors.

**Domain-Specific Terminology**

**Behavioral Role**
The specific role or function an NPC assumes, influenced by its mind state, such as Warrior, Archer, or Mage.

**Special Ability**
A unique skill or action that an NPC can perform, typically tied to its mind state or role, such as Charge or Fireball.

**Command Range**
The distance within which an NPC can issue commands or exert influence, often used in the context of leadership roles like Commander.

**Perception**
A measure of how well an NPC can detect or sense elements in the environment, influencing behaviors like scouting or detecting enemies.

**Patrol Points**
Predetermined locations that a Guard or similar NPC will move between as part of their patrol duties.
