""" trigger/66000004_gd/cannon.xml """
import common


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[104]):
            return 대포등장(self.ctx)


class 대포등장(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001,1002,1003,1004], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[104]):
            return 소환해제(self.ctx)


class 소환해제(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1001,1002,1003,1004], arg2=False)


initial_state = 시작
