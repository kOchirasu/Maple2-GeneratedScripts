""" trigger/52000014_qd/rockdrop_1500.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[1500], enable=False)
        self.set_skill(triggerIds=[1502], enable=False)
        self.set_skill(triggerIds=[1504], enable=False)
        self.set_effect(triggerIds=[1501], visible=False) # RockDrop
        self.set_effect(triggerIds=[1503], visible=False) # RockDrop
        self.set_effect(triggerIds=[1505], visible=False) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 낙하01시작(self.ctx)


class 낙하01시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[1501], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return 낙하01완료(self.ctx)


class 낙하01완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_skill(triggerIds=[1500], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 낙하02시작(self.ctx)


class 낙하02시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[1503], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return 낙하02완료(self.ctx)


class 낙하02완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='3', seconds=1)
        self.set_skill(triggerIds=[1502], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='3'):
            return 낙하03시작(self.ctx)


class 낙하03시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[1505], visible=True) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1200):
            return 낙하03완료(self.ctx)


class 낙하03완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='4', seconds=2)
        self.set_skill(triggerIds=[1504], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='4'):
            return 초기화(self.ctx)


class 초기화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_timer(timerId='5', seconds=1)
        self.set_skill(triggerIds=[1500], enable=False)
        self.set_skill(triggerIds=[1502], enable=False)
        self.set_skill(triggerIds=[1504], enable=False)
        self.set_effect(triggerIds=[1501], visible=False) # RockDrop
        self.set_effect(triggerIds=[1503], visible=False) # RockDrop
        self.set_effect(triggerIds=[1505], visible=False) # RockDrop

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='5'):
            return 낙하01시작(self.ctx)


initial_state = 대기
