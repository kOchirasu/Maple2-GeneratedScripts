""" trigger/52000014_qd/rockdrop_1400.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_skill(triggerIds=[1400], enable=False)
        self.set_effect(triggerIds=[1401], visible=False) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 낙하01준비(self.ctx)


class 낙하01준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 낙하01시작(self.ctx)


class 낙하01시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[1401], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return 낙하01완료(self.ctx)


class 낙하01완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='2', seconds=1)
        self.set_skill(triggerIds=[1400], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='2'):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='3', seconds=1)
        self.set_skill(triggerIds=[1400], enable=False)
        self.set_effect(triggerIds=[1401], visible=False) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 낙하01준비(self.ctx)


initial_state = 대기
