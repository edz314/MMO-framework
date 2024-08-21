# fsm_controller.py

class FSMController:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state_name, state):
        """
        Adds a new state to the FSM.
        
        :param state_name: The name of the state.
        :param state: An instance of the state class (must implement enter, execute, exit methods).
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

    def execute_state(self):
        """
        Executes the logic of the current state.
        """
        if self.current_state:
            self.current_state.execute()

    def get_current_state(self):
        """
        Returns the name of the current state.
        
        :return: The name of the current state.
        """
        return self.current_state.__class__.__name__ if self.current_state else None


# Example Mind State Classes:

class IdleState:
    def enter(self):
        print("Entering Idle State")

    def execute(self):
        print("NPC is idle.")

    def exit(self):
        print("Exiting Idle State")


class PatrolState:
    def enter(self):
        print("Entering Patrol State")

    def execute(self):
        print("NPC is patrolling.")

    def exit(self):
        print("Exiting Patrol State")


class AttackState:
    def enter(self):
        print("Entering Attack State")

    def execute(self):
        print("NPC is attacking.")

    def exit(self):
        print("Exiting Attack State")


class FleeState:
    def enter(self):
        print("Entering Flee State")

    def execute(self):
        print("NPC is fleeing.")

    def exit(self):
        print("Exiting Flee State")

# Additional mind states can be added here...


# Example of integrating these states with FSMController:

def main():
    fsm = FSMController()

    # Add all necessary states
    fsm.add_state("Idle", IdleState())
    fsm.add_state("Patrol", PatrolState())
    fsm.add_state("Attack", AttackState())
    fsm.add_state("Flee", FleeState())
    # Add more states as needed...

    # Example transitions
    fsm.transition_to("Idle")
    fsm.execute_state()

    fsm.transition_to("Patrol")
    fsm.execute_state()

    fsm.transition_to("Attack")
    fsm.execute_state()

    fsm.transition_to("Flee")
    fsm.execute_state()


if __name__ == "__main__":
    main()

