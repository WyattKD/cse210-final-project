from game import constants
from game.actions.action import Action

class UpdateUI(Action):

    def __init__(self):
        super().__init__()

    def execute(self, cast):
        self.update_hp_bar(cast)

    def update_hp_bar(self, cast):
        hp_bar = cast["UI"][0]
        player = cast["players"][0]
        hp = player.get_hp()
        if hp == 3:
            hp_bar.set_image(constants.HP_BAR_3)
        elif hp == 2:
            hp_bar.set_image(constants.HP_BAR_2)
        elif hp == 1:
            hp_bar.set_image(constants.HP_BAR_1)
        else:
            hp_bar.set_image(constants.HP_BAR_0)
