""" trigger/02020101_bf/dummysummon.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Dummy', value=1):
            self.create_monster(spawnIds=[401], animationEffect=False)
            return 더미소환(self.ctx)


class 더미소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=900008, key='Dummy', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101]):
            return 대기(self.ctx)
        if self.user_value(key='Dummy', value=0):
            return 대기(self.ctx)


initial_state = 대기
