""" trigger/02000066_bf/effect.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=103, spawnIds=[99]):
            return 이펙트생성(self.ctx)


class 이펙트생성(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[6001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[99]):
            return 이펙트소멸(self.ctx)


class 이펙트소멸(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='15', seconds=15)
        self.set_effect(triggerIds=[6001], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='15'):
            return 시작(self.ctx)


initial_state = 시작
