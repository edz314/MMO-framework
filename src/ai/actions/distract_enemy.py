# src/ai/actions/distract_enemy.py

from .action import Action

class DistractEnemyAction(Action):
    def __init__(self):
        super().__init__(name="Distract Enemy", prerequisites=None)

    def execute(self, npc, environment):
        print(f"{npc.name} is distracting the enemy!")
        # Implement logic to distract the enemy, diverting their attention
        enemy = environment.get_closest_enemy(npc)
        if enemy:
            enemy.get_distracted_by(npc)
