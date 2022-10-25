""" trigger/02000355_bf/actor11.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[611], visible=False)
        self.set_actor(triggerId=211, visible=True, initialSequence='Damg_B')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[11001]):
            return 몬스터소환대기(self.ctx)


class 몬스터소환대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[611], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 몬스터소환(self.ctx)


class 몬스터소환(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2011], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 더미해제(self.ctx)


class 더미해제(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=211, visible=False, initialSequence='Damg_B')

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2011]):
            return 소멸(self.ctx)
        if self.monster_dead(boxIds=[2099]):
            return 소멸(self.ctx)
        if self.npc_detected(boxId=105, spawnIds=[2011]):
            self.destroy_monster(spawnIds=[2011])
            return 리젠준비(self.ctx)


class 대기시간(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=30000):
            return 리젠준비(self.ctx)
        if self.monster_dead(boxIds=[2099]):
            return 소멸(self.ctx)


class 리젠준비(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=211, visible=True, initialSequence='Regen_A')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return 대기(self.ctx)


class 소멸(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2011])


initial_state = 대기
