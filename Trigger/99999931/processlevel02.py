""" trigger/99999931/processlevel02.xml """
from common import *
import state


class 레버당기기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000218], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000218], arg2=0):
            return 카운트다운1()


class 카운트다운1(state.State):
    def on_enter(self):
        set_timer(timerId='31', seconds=1)
        set_event_ui(type=1, arg2='3', arg3='1000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='31'):
            return 카운트다운2()


class 카운트다운2(state.State):
    def on_enter(self):
        set_timer(timerId='32', seconds=1)
        set_event_ui(type=1, arg2='2', arg3='1000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='32'):
            return 카운트다운3()


class 카운트다운3(state.State):
    def on_enter(self):
        set_timer(timerId='33', seconds=1)
        set_event_ui(type=1, arg2='1', arg3='1000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='33'):
            return 게임시작()


class 게임시작(state.State):
    def on_enter(self):
        set_timer(timerId='34', seconds=1) # arg2는 시간 (초)
        set_breakable(triggerIds=[103,104,108,111,113,115,116,118,119,121,122,124,126,129,133,134], enabled=True) # 움직이는 발판을 이동한다 (arg2=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='34'):
            return 게임진행1()


class 게임진행1(state.State):
    def on_enter(self):
        set_timer(timerId='35', seconds=1) # arg2는 시간 (초)
        set_breakable(triggerIds=[103,104,108,111,113,115,116,118,119,121,122,124,126,129,133,134], enabled=False) # 움직이는 발판을 멈춘다 (arg2=0)
        set_skill(triggerIds=[803], isEnable=True)
        set_skill(triggerIds=[804], isEnable=True)
        set_skill(triggerIds=[808], isEnable=True)
        set_skill(triggerIds=[811], isEnable=True)
        set_skill(triggerIds=[813], isEnable=True)
        set_skill(triggerIds=[815], isEnable=True)
        set_skill(triggerIds=[816], isEnable=True)
        set_skill(triggerIds=[818], isEnable=True)
        set_skill(triggerIds=[819], isEnable=True)
        set_skill(triggerIds=[821], isEnable=True)
        set_skill(triggerIds=[822], isEnable=True)
        set_skill(triggerIds=[824], isEnable=True)
        set_skill(triggerIds=[826], isEnable=True)
        set_skill(triggerIds=[829], isEnable=True)
        set_skill(triggerIds=[833], isEnable=True)
        set_skill(triggerIds=[834], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='35'):
            return 게임진행2()


class 게임진행2(state.State):
    def on_enter(self):
        set_timer(timerId='36', seconds=2) # arg2는 시간 (초)
        set_skill(triggerIds=[803], isEnable=False)
        set_skill(triggerIds=[804], isEnable=False)
        set_skill(triggerIds=[808], isEnable=False)
        set_skill(triggerIds=[811], isEnable=False)
        set_skill(triggerIds=[813], isEnable=False)
        set_skill(triggerIds=[815], isEnable=False)
        set_skill(triggerIds=[816], isEnable=False)
        set_skill(triggerIds=[818], isEnable=False)
        set_skill(triggerIds=[819], isEnable=False)
        set_skill(triggerIds=[821], isEnable=False)
        set_skill(triggerIds=[822], isEnable=False)
        set_skill(triggerIds=[824], isEnable=False)
        set_skill(triggerIds=[826], isEnable=False)
        set_skill(triggerIds=[829], isEnable=False)
        set_skill(triggerIds=[833], isEnable=False)
        set_skill(triggerIds=[834], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='36'):
            return 레버당기기()


