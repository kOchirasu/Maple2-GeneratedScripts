""" trigger/02010057_bf/main.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102,103], animationEffect=True)


initial_state = 시작
