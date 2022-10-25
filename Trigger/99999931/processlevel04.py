""" trigger/99999931/processlevel04.xml """
import common


class 레버당기기(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10000220], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10000220], stateValue=0):
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
        self.set_breakable(triggerIds=[101,102,104,105,107,108,111,112,114,115,117,118,120,121,122,123,125,126,128,129,130,131,132,135,136], enable=True) # 움직이는 발판을 이동한다 (arg2=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='34'):
            return 게임진행1(self.ctx)


class 게임진행1(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='35', seconds=1) # arg2는 시간 (초)
        self.set_breakable(triggerIds=[101,102,104,105,107,108,111,112,114,115,117,118,120,121,122,123,125,126,128,129,130,131,132,135,136], enable=False) # 움직이는 발판을 멈춘다 (arg2=0)
        self.set_skill(triggerIds=[801], enable=True)
        self.set_skill(triggerIds=[802], enable=True)
        self.set_skill(triggerIds=[804], enable=True)
        self.set_skill(triggerIds=[805], enable=True)
        self.set_skill(triggerIds=[807], enable=True)
        self.set_skill(triggerIds=[808], enable=True)
        self.set_skill(triggerIds=[811], enable=True)
        self.set_skill(triggerIds=[812], enable=True)
        self.set_skill(triggerIds=[814], enable=True)
        self.set_skill(triggerIds=[815], enable=True)
        self.set_skill(triggerIds=[817], enable=True)
        self.set_skill(triggerIds=[818], enable=True)
        self.set_skill(triggerIds=[820], enable=True)
        self.set_skill(triggerIds=[821], enable=True)
        self.set_skill(triggerIds=[822], enable=True)
        self.set_skill(triggerIds=[823], enable=True)
        self.set_skill(triggerIds=[825], enable=True)
        self.set_skill(triggerIds=[826], enable=True)
        self.set_skill(triggerIds=[828], enable=True)
        self.set_skill(triggerIds=[829], enable=True)
        self.set_skill(triggerIds=[830], enable=True)
        self.set_skill(triggerIds=[831], enable=True)
        self.set_skill(triggerIds=[832], enable=True)
        self.set_skill(triggerIds=[835], enable=True)
        self.set_skill(triggerIds=[836], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='35'):
            return 게임진행2(self.ctx)


class 게임진행2(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='36', seconds=2) # arg2는 시간 (초)
        self.set_skill(triggerIds=[801], enable=False)
        self.set_skill(triggerIds=[802], enable=False)
        self.set_skill(triggerIds=[804], enable=False)
        self.set_skill(triggerIds=[805], enable=False)
        self.set_skill(triggerIds=[807], enable=False)
        self.set_skill(triggerIds=[808], enable=False)
        self.set_skill(triggerIds=[811], enable=False)
        self.set_skill(triggerIds=[812], enable=False)
        self.set_skill(triggerIds=[814], enable=False)
        self.set_skill(triggerIds=[815], enable=False)
        self.set_skill(triggerIds=[817], enable=False)
        self.set_skill(triggerIds=[818], enable=False)
        self.set_skill(triggerIds=[820], enable=False)
        self.set_skill(triggerIds=[821], enable=False)
        self.set_skill(triggerIds=[822], enable=False)
        self.set_skill(triggerIds=[823], enable=False)
        self.set_skill(triggerIds=[825], enable=False)
        self.set_skill(triggerIds=[826], enable=False)
        self.set_skill(triggerIds=[828], enable=False)
        self.set_skill(triggerIds=[829], enable=False)
        self.set_skill(triggerIds=[830], enable=False)
        self.set_skill(triggerIds=[831], enable=False)
        self.set_skill(triggerIds=[832], enable=False)
        self.set_skill(triggerIds=[835], enable=False)
        self.set_skill(triggerIds=[836], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='36'):
            return 레버당기기(self.ctx)


initial_state = 레버당기기
