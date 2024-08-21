import unittest
from unittest.mock import Mock
from src.ai.npc_mind import NPCMind
from src.data.npc_data import NPCData

class MockEnvironment:
    def is_enemy_nearby(self, npc):
        return False

    def update_conditions(self):
        pass

class TestNPCMind(unittest.TestCase):

    def setUp(self):
        # Set up any initial state here before each test
        self.npc_data = NPCData(name="TestNPC", health=100, inventory=["sword", "shield"])
        self.npc_mind = NPCMind(self.npc_data)
        self.environment = MockEnvironment()

    def test_initial_state(self):
        # Test the initial state of the NPC
        self.assertEqual(self.npc_data.health, 100)
        self.assertEqual(self.npc_data.get_current_state_name(), "Neutral")

    def test_switch_mind_type_success(self):
        # Test switching mind types successfully
        self.npc_mind.fsm.switch_mind_type("Warrior")
        self.assertEqual(self.npc_data.current_mind_type, "Warrior")

    def test_switch_mind_type_failure(self):
        # Test switching mind types when required items are missing
        self.npc_mind.fsm.switch_mind_type("Mage")  # NPC lacks "staff" and "spellbook"
        self.assertNotEqual(self.npc_data.current_mind_type, "Mage")

    def test_fsm_state_execution(self):
        # Test FSM state execution based on mind type
        self.npc_mind.fsm.switch_mind_type("Warrior")
        self.npc_mind.update(self.environment)
        # Additional assertions to ensure correct behavior during state execution

    def tearDown(self):
        # Clean up after each test if necessary
        pass

if __name__ == '__main__':
    unittest.main()
