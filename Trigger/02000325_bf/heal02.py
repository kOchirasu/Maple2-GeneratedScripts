""" trigger/02000325_bf/heal02.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_skill(triggerIds=[702], isEnable=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000740], arg2=0):
            return 스킬작동()


class 스킬작동(state.State):
    def on_enter(self):
        set_skill(triggerIds=[702], isEnable=True)
        set_timer(timerId='1', seconds=1)
        set_effect(triggerIds=[612], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            set_skill(triggerIds=[702], isEnable=False)
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            set_interact_object(triggerIds=[10000740], state=2)
            return 시작()


