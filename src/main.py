from src.ai.fsm.fsm_controller import FSMController
from mind_state_library import MindStateIdle, MindStatePatrol, MindStateAttack

def main():
    fsm = FSMController()

    # Add states from the Mind State library
    fsm.add_state("Idle", MindStateIdle(fsm))
    fsm.add_state("Patrol", MindStatePatrol(fsm))
    fsm.add_state("Attack", MindStateAttack(fsm))
    # Add other states as needed...

    # Example transitions
    fsm.transition_to("Idle")
    fsm.execute_state()

    fsm.transition_to("Patrol")
    fsm.execute_state()

    fsm.transition_to("Attack")
    fsm.execute_state()

if __name__ == "__main__":
    main()
