# fsm_state.py

from abc import ABC, abstractmethod

class FSMState(ABC):
    """
    Abstract base class for all FSM states. Each state must implement the enter, execute, and exit methods.
    """
    
    def __init__(self, fsm_controller):
        """
        Initializes the FSMState with a reference to the FSM controller.

        :param fsm_controller: The FSMController that manages this state.
        """
        self.fsm_controller = fsm_controller

    @abstractmethod
    def enter(self):
        """
        This method is called when the state is entered.
        """
        pass

    @abstractmethod
    def execute(self):
        """
        This method is called on each game tick while the state is active.
        """
        pass

    @abstractmethod
    def exit(self):
        """
        This method is called when the state is exited.
        """
        pass

    def transition_to(self, state_name):
        """
        Utility method for transitioning to another state.

        :param state_name: The name of the state to transition to.
        """
        self.fsm_controller.transition_to(state_name)

