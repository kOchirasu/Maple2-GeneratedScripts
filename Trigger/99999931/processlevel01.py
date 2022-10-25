""" trigger/99999931/processlevel01.xml """
import common


class 레버당기기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000217], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000217], stateValue=0):
            return 카운트다운1(self.ctx)


class 카운트다운1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='31', seconds=1)
        self.set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='31'):
            return 카운트다운2(self.ctx)


class 카운트다운2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='32', seconds=1)
        self.set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='32'):
            return 카운트다운3(self.ctx)


class 카운트다운3(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='33', seconds=1)
        self.set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='33'):
            return 게임시작(self.ctx)


class 게임시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='34', seconds=1) # arg2는 시간 (초)
        self.set_breakable(triggerIds=[101,102,103,104,105,106,107,114,115,116,118,119,121,123,126,130,131,132,133,134,135], enable=True) # 움직이는 발판을 이동한다 (arg2=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='34'):
            return 게임진행1(self.ctx)


class 게임진행1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='35', seconds=1) # arg2는 시간 (초)
        self.set_breakable(triggerIds=[101,102,103,104,105,106,107,114,115,116,118,119,121,123,126,130,131,132,133,134,135], enable=False) # 움직이는 발판을 멈춘다 (arg2=0)
        self.set_skill(triggerIds=[801,802,803,804,805,806,807], isEnable='1')
        self.set_skill(triggerIds=[814], enable=True)
        self.set_skill(triggerIds=[815], enable=True)
        self.set_skill(triggerIds=[816], enable=True)
        self.set_skill(triggerIds=[818], enable=True)
        self.set_skill(triggerIds=[819], enable=True)
        self.set_skill(triggerIds=[821], enable=True)
        self.set_skill(triggerIds=[823], enable=True)
        self.set_skill(triggerIds=[826], enable=True)
        self.set_skill(triggerIds=[830], enable=True)
        self.set_skill(triggerIds=[831], enable=True)
        self.set_skill(triggerIds=[832], enable=True)
        self.set_skill(triggerIds=[833], enable=True)
        self.set_skill(triggerIds=[834], enable=True)
        self.set_skill(triggerIds=[835], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='35'):
            return 게임진행2(self.ctx)


class 게임진행2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='36', seconds=2) # arg2는 시간 (초)
        self.set_skill(triggerIds=[801], enable=False)
        self.set_skill(triggerIds=[802], enable=False)
        self.set_skill(triggerIds=[803], enable=False)
        self.set_skill(triggerIds=[804], enable=False)
        self.set_skill(triggerIds=[805], enable=False)
        self.set_skill(triggerIds=[806], enable=False)
        self.set_skill(triggerIds=[807], enable=False)
        self.set_skill(triggerIds=[814], enable=False)
        self.set_skill(triggerIds=[815], enable=False)
        self.set_skill(triggerIds=[816], enable=False)
        self.set_skill(triggerIds=[818], enable=False)
        self.set_skill(triggerIds=[819], enable=False)
        self.set_skill(triggerIds=[821], enable=False)
        self.set_skill(triggerIds=[823], enable=False)
        self.set_skill(triggerIds=[826], enable=False)
        self.set_skill(triggerIds=[830], enable=False)
        self.set_skill(triggerIds=[831], enable=False)
        self.set_skill(triggerIds=[832], enable=False)
        self.set_skill(triggerIds=[833], enable=False)
        self.set_skill(triggerIds=[834], enable=False)
        self.set_skill(triggerIds=[835], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='36'):
            return 레버당기기(self.ctx)


initial_state = 레버당기기
