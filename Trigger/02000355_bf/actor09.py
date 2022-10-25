""" trigger/02000355_bf/actor09.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[609], visible=False)
        self.set_actor(triggerId=209, visible=True, initialSequence='Damg_B')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1901]):
            return 몬스터소환대기(self.ctx)


class 몬스터소환대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[609], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3500):
            return 몬스터소환(self.ctx)


class 몬스터소환(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2009], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return 더미해제(self.ctx)


class 더미해제(common.Trigger):
    def on_enter(self):
        self.set_actor(triggerId=209, visible=False, initialSequence='Damg_B')

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2009]):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
