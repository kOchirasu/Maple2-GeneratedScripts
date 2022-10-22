""" trigger/02000136_ad/01_trigger02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[801,802,803], visible=False)
        set_interact_object(triggerIds=[10000067], state=1)
        set_mesh(triggerIds=[14,17,16], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000067], arg2=0):
            return 발판등장1()


class 발판등장1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[14], visible=True)
        set_effect(triggerIds=[801], visible=True)
        set_timer(timerId='2', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 발판등장2()


class 발판등장2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[17], visible=True)
        set_effect(triggerIds=[802], visible=True)
        set_timer(timerId='3', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 발판등장3()


class 발판등장3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[16], visible=True)
        set_effect(triggerIds=[803], visible=True)
        set_timer(timerId='4', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 대기()


