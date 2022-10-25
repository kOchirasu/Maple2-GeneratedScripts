""" trigger/02100004_bf/npc12.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[101]):
            return 소환대기(self.ctx)


class 소환대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999992, key='NpcSpawned12', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='NpcSpawn12', value=1):
            return 소환(self.ctx)


class 소환(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=999992, key='NpcSpawned12', value=1)
        self.create_monster(spawnIds=[2012], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
