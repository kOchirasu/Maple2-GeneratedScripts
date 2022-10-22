""" trigger/02000066_bf/buffskill.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return A스킬작동()


class A스킬작동(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6002], visible=False)
        set_skill(triggerIds=[7001], isEnable=True)
        set_timer(timerId='60', seconds=60)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            set_skill(triggerIds=[7001], isEnable=False)
            set_effect(triggerIds=[6002], visible=False)
            return 시작대기중()


