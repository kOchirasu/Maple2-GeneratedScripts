""" trigger/02020111_bf/summon_02.xml """
import trigger_api


class 시작(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 소환준비(self.ctx)


class 소환준비(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon_Enemy_1', value=0):
            return 시작(self.ctx)
        if self.user_value(key='Summon_Enemy_1', value=1):
            return 몬스터등장(self.ctx)


class 몬스터등장(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[121,122,123,124,131,132,133,134])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon_Enemy_1', value=0):
            return 시작(self.ctx)
        if self.user_value(key='Summon_Enemy_2', value=1):
            return 몬스터등장_2(self.ctx)


class 몬스터등장_2(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[121,122,123,124,131,132,133,134])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon_Enemy_1', value=0):
            return 시작(self.ctx)


initial_state = 시작
