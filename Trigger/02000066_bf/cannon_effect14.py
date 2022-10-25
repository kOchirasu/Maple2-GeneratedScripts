""" trigger/02000066_bf/cannon_effect14.xml """
import common


class 시작(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[814], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[124]):
            return 이펙트대기(self.ctx)


class 이펙트대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.npc_detected(boxId=124, spawnIds=[8014]):
            return 이펙트on(self.ctx)


class 이펙트on(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[814], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[8014]):
            return 대기시간(self.ctx)
        if not self.user_detected(boxIds=[124]):
            return 대기시간(self.ctx)


class 대기시간(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[814], visible=False)
        self.set_timer(timerId='2', seconds=2)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='2'):
            return 시작(self.ctx)


initial_state = 시작
