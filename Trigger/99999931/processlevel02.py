""" trigger/99999931/processlevel02.xml """
import trigger_api


class 레버당기기(trigger_api.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000218], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000218], stateValue=0):
            return 카운트다운1(self.ctx)


class 카운트다운1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='31', seconds=1)
        self.set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='31'):
            return 카운트다운2(self.ctx)


class 카운트다운2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='32', seconds=1)
        self.set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='32'):
            return 카운트다운3(self.ctx)


class 카운트다운3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='33', seconds=1)
        self.set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='33'):
            return 게임시작(self.ctx)


class 게임시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='34', seconds=1) # arg2는 시간 (초)
        self.set_breakable(triggerIds=[103,104,108,111,113,115,116,118,119,121,122,124,126,129,133,134], enable=True) # 움직이는 발판을 이동한다 (arg2=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='34'):
            return 게임진행1(self.ctx)


class 게임진행1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='35', seconds=1) # arg2는 시간 (초)
        self.set_breakable(triggerIds=[103,104,108,111,113,115,116,118,119,121,122,124,126,129,133,134], enable=False) # 움직이는 발판을 멈춘다 (arg2=0)
        self.set_skill(triggerIds=[803], enable=True)
        self.set_skill(triggerIds=[804], enable=True)
        self.set_skill(triggerIds=[808], enable=True)
        self.set_skill(triggerIds=[811], enable=True)
        self.set_skill(triggerIds=[813], enable=True)
        self.set_skill(triggerIds=[815], enable=True)
        self.set_skill(triggerIds=[816], enable=True)
        self.set_skill(triggerIds=[818], enable=True)
        self.set_skill(triggerIds=[819], enable=True)
        self.set_skill(triggerIds=[821], enable=True)
        self.set_skill(triggerIds=[822], enable=True)
        self.set_skill(triggerIds=[824], enable=True)
        self.set_skill(triggerIds=[826], enable=True)
        self.set_skill(triggerIds=[829], enable=True)
        self.set_skill(triggerIds=[833], enable=True)
        self.set_skill(triggerIds=[834], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='35'):
            return 게임진행2(self.ctx)


class 게임진행2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='36', seconds=2) # arg2는 시간 (초)
        self.set_skill(triggerIds=[803], enable=False)
        self.set_skill(triggerIds=[804], enable=False)
        self.set_skill(triggerIds=[808], enable=False)
        self.set_skill(triggerIds=[811], enable=False)
        self.set_skill(triggerIds=[813], enable=False)
        self.set_skill(triggerIds=[815], enable=False)
        self.set_skill(triggerIds=[816], enable=False)
        self.set_skill(triggerIds=[818], enable=False)
        self.set_skill(triggerIds=[819], enable=False)
        self.set_skill(triggerIds=[821], enable=False)
        self.set_skill(triggerIds=[822], enable=False)
        self.set_skill(triggerIds=[824], enable=False)
        self.set_skill(triggerIds=[826], enable=False)
        self.set_skill(triggerIds=[829], enable=False)
        self.set_skill(triggerIds=[833], enable=False)
        self.set_skill(triggerIds=[834], enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='36'):
            return 레버당기기(self.ctx)


initial_state = 레버당기기
