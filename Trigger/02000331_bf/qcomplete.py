""" trigger/02000331_bf/qcomplete.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='clearafter', value=0)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9032], questIds=[10003065], questStates=[2]):
            return 완료npc리젠(self.ctx)


class 완료npc리젠(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[112])

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='clearafter', value=1):
            return 완료npc킬(self.ctx)


class 완료npc킬(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[112])


initial_state = 대기
