""" trigger/02100004_bf/npc13.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[101]):
            return 소환대기(self.ctx)


class 소환대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=999992, key='NpcSpawned13', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='NpcSpawn13', value=1):
            return 소환(self.ctx)


class 소환(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=999992, key='NpcSpawned13', value=1)
        self.create_monster(spawnIds=[2013], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
