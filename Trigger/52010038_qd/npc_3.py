""" trigger/52010038_qd/npc_3.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6203], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='GaugeStart', value=1):
            return npc체크(self.ctx)


class npc체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_in_combat(boxIds=[1803]):
            return 이펙트(self.ctx)
        if not self.monster_in_combat(boxIds=[1803]):
            return 생성(self.ctx)
        if self.user_value(key='GaugeClosed', value=1):
            return 종료(self.ctx)


class 이펙트(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6203], visible=True)

    def on_tick(self) -> common.Trigger:
        if not self.monster_in_combat(boxIds=[1803]):
            return 생성(self.ctx)


class 생성(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6203], visible=False)
        self.init_npc_rotation(spawnIds=[1803])
        self.create_monster(spawnIds=[4000], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return npc체크(self.ctx)
        if self.user_value(key='GaugeClosed', value=1):
            return 종료(self.ctx)


class 종료(common.Trigger):
    pass


initial_state = 대기
