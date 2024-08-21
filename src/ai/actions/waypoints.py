# src/ai/actions/waypoints.py

from .action import Action

class WaypointsAction(Action):
    def __init__(self):
        super().__init__(name="Waypoints", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is following waypoints.")
        # Implement logic to follow a series of waypoints
        waypoints = environment.get_waypoints(npc)
        npc.follow_waypoints(waypoints)
