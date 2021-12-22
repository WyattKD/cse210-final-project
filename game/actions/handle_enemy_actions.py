from game.actions.action import Action

class HandleEnemyActions(Action):

    def __init__(self, audio_service):
        super().__init__()
        self._audio_service = audio_service

    def execute(self, cast):
        enemies = cast["enemies"]
        player = cast["players"][0]
        for enemy in enemies:
            enemy.move(player)
        for enemy in enemies:
            if enemy.has_shot_sound():
                enemy.shoot(cast, self._audio_service)