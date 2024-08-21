# src/ai/fsm/fsm_controller.py

class FSMController:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state_name, state):
        """
        Adds a new state to the FSM.
        :param state_name: The name of the state.
        :param state: An instance of the state class.
        """
        self.states[state_name] = state

    def transition_to(self, state_name):
        """
        Transitions to a new state.
        :param state_name: The name of the state to transition to.
        """
        if self.current_state:
            self.current_state.exit()
        
        self.current_state = self.states.get(state_name)
        
        if self.current_state:
            self.current_state.enter()

    def execute_state(self, npc, environment):
        """
        Executes the logic of the current state.
        :param npc: The NPC being controlled.
        :param environment: The environment or context in which the NPC operates.
        """
        if self.current_state:
            self.current_state.execute(npc, environment)

    def get_current_state(self):
        """
        Returns the name of the current state.
        :return: The name of the current state.
        """
        return self.current_state.__class__.__name__ if self.current_state else None

class FSMState:
    def __init__(self, fsm_controller):
        self.fsm_controller = fsm_controller
        self.actions = []

    def enter(self, npc):
        """Called when the state is entered."""
        pass

    def execute(self, npc, environment):
        """Executes the state's logic, selecting and performing actions."""
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

    def exit(self, npc):
        """Called when the state is exited."""
        pass

    def can_enter(self, npc, environment):
        """Determines if the NPC can enter this state."""
        return True

