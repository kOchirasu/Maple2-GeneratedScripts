""" trigger/02020061_bf/object_monsterspawn.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[482], isStart=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='EliteSpawn', value=1):
            return 스폰(self.ctx)


class 스폰(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[482], isStart=True)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='EliteSpawn', value=0):
            return 대기(self.ctx)
        if self.user_value(key='EliteSpawn', value=2):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[482], isStart=False)


initial_state = 대기
