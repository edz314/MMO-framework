# src/ai/actions/patrol.py

from .action import Action

class PatrolAction(Action):
    def __init__(self):
        super().__init__(name="Patrol", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is patrolling the area!")
        # Implement logic to patrol between waypoints or along a path
        patrol_route = environment.get_patrol_route(npc)
        npc.follow_route(patrol_route)
