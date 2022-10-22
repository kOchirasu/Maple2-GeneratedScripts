""" trigger/02000118_bf/earthquake02.xml """
from common import *
import state


class 레버당기기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000291], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000291], arg2=0):
            return 스킬동작()


class 스킬동작(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        set_skill(triggerIds=[2005], isEnable=True)
        set_skill(triggerIds=[2006], isEnable=True)
        set_skill(triggerIds=[2007], isEnable=True)
        set_skill(triggerIds=[2008], isEnable=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=10) # arg2는 시간 (초)
        set_skill(triggerIds=[2005], isEnable=False)
        set_skill(triggerIds=[2006], isEnable=False)
        set_skill(triggerIds=[2007], isEnable=False)
        set_skill(triggerIds=[2008], isEnable=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 레버당기기()


