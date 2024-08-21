# 8 - Strategic.py

from src.ai.fsm.fsm_state import FSMState

class StrategicState(FSMState):
    """
    Strategic State for NPCs. This state is used when the NPC is in a strategic mode,
    focusing on long-term planning, resource management, and making calculated decisions to achieve objectives.
    """

    def enter(self):
        """
        Called when the NPC enters the Strategic state. Sets up any necessary parameters.
        """
        print("NPC has entered Strategic State")
        # Example: Set planning level high and focus on long-term goals
        self.fsm_controller.npc_data.planning_level = 100
        self.fsm_controller.npc_data.resource_management = 100

    def execute(self):
        """
        Called on each game tick while in the Strategic state. Executes strategic behaviors.
        """
        print("NPC is making strategic decisions...")
        # Example: Assess the situation, allocate resources, and make calculated moves
        if self.analyze_situation():
            self.plan_and_execute()
        else:
            self.adjust_strategy()

    def exit(self):
        """
        Called when transitioning out of the Strategic state. Resets parameters to normal.
        """
        print("NPC is exiting Strategic State")
        # Example: Reset planning level and resource management
        self.fsm_controller.npc_data.planning_level = 50
        self.fsm_controller.npc_data.resource_management = 50

    def analyze_situation(self):
        """
        Analyze the current situation to make informed decisions.
        :return: True if the current strategy is effective, False otherwise.
        """
        # Placeholder logic for analyzing the situation
        return True  # Replace with actual analysis logic

    def plan_and_execute(self):
        """
        Plan and execute strategic moves based on the analysis.
        """
        print("NPC is executing a strategic plan!")

    def adjust_strategy(self):
        """
        Adjust the strategy if the current plan is not effective.
        """
        print("NPC is adjusting its strategy to adapt to the situation.")
