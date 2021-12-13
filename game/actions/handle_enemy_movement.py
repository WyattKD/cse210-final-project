from game.actions.action import Action

class HandleEnemyMovement(Action):

    def __init__(self):
        super().__init__()

    def execute(self, cast):
        enemies = cast["enemies"]
        player = cast["players"][0]
        for enemy in enemies:
            enemy.move(player)