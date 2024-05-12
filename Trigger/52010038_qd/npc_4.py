""" trigger/52010038_qd/npc_4.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6204], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='GaugeStart', value=1):
            return npc체크(self.ctx)


class npc체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_in_combat(boxIds=[1804]):
            return 이펙트(self.ctx)
        if not self.monster_in_combat(boxIds=[1804]):
            return 생성(self.ctx)
        if self.user_value(key='GaugeClosed', value=1):
            return 종료(self.ctx)


class 이펙트(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6204], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.monster_in_combat(boxIds=[1804]):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6204], visible=False)
        self.init_npc_rotation(spawnIds=[1804])
        self.create_monster(spawnIds=[4000], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return npc체크(self.ctx)
        if self.user_value(key='GaugeClosed', value=1):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
