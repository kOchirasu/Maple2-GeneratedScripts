""" trigger/52010018_qd/main_3.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1001], animationEffect=False)
        self.create_monster(spawnIds=[1005], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 분기점(self.ctx)


class 분기점(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[100], questIds=[10002851], questStates=[2]):
            self.destroy_monster(spawnIds=[1005])
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[100], questIds=[10002852], questStates=[1]):
            self.destroy_monster(spawnIds=[1005])
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[100], questIds=[10002853], questStates=[1]):
            self.destroy_monster(spawnIds=[1005])
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[100], questIds=[10002853], questStates=[2]):
            self.destroy_monster(spawnIds=[1005])
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[100], questIds=[10002851], questStates=[3]):
            return 분기점2(self.ctx)


class 분기점2(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[100], questIds=[10002852], questStates=[2]):
            return 종료(self.ctx)
        if self.quest_user_detected(boxIds=[100], questIds=[10002852], questStates=[3]):
            return 종료(self.ctx)
        if not self.quest_user_detected(boxIds=[100], questIds=[10002852], questStates=[2]):
            self.destroy_monster(spawnIds=[1005])
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
