# src/ai/fsm/fsm_state.py

from abc import ABC, abstractmethod

class FSMState(ABC):
    def __init__(self, fsm_controller):
        self.fsm_controller = fsm_controller
        self.actions = []

    @abstractmethod
    def can_enter(self, npc, environment):
        """
        Determine if the NPC can enter this state.
        :param npc: The NPC in question.
        :param environment: The environment or context in which the NPC operates.
        :return: True if the NPC can enter this state, otherwise False.
        """
        pass

    @abstractmethod
    def enter(self, npc):
        """
        Called when the state is entered.
        :param npc: The NPC entering the state.
        """
        pass

    @abstractmethod
    def execute(self, npc, environment):
        """
        Executes the state's logic, selecting and performing actions.
        :param npc: The NPC performing actions.
        :param environment: The environment or context in which the NPC operates.
        """
        for action in self.actions:
            if action.can_execute(npc):
                action.execute(npc, environment)
                break

    @abstractmethod
    def exit(self, npc):
        """
        Called when the state is exited.
        :param npc: The NPC exiting the state.
        """
        pass
