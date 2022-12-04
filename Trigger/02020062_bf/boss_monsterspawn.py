""" trigger/02020062_bf/boss_monsterspawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[494], isStart=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterSpawn', value=1):
            return 스폰(self.ctx)


class 스폰(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[494], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='MonsterSpawn', value=0):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[494], isStart=False)


initial_state = 대기
