""" trigger/02020061_bf/object_monsterspawn.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[482])

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteSpawn') >= 1:
            return 스폰(self.ctx)


class 스폰(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[482], is_start=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='EliteSpawn') >= 0:
            return 대기(self.ctx)
        if self.user_value(key='EliteSpawn') >= 2:
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.start_combine_spawn(group_id=[482])


initial_state = 대기
