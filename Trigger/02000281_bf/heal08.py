""" trigger/02000281_bf/heal08.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_skill(triggerIds=[708], isEnable=False)
        set_interact_object(triggerIds=[10000247], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000247], arg2=0):
            return 스킬작동()


class 스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[708], isEnable=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            set_skill(triggerIds=[708], isEnable=False)
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_timer(timerId='29', seconds=29)

    def on_tick(self) -> state.State:
        if time_expired(timerId='29'):
            return 시작()


