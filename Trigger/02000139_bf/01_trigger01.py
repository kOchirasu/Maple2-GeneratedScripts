""" trigger/02000139_bf/01_trigger01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[401,402,403,404], visible=False)
        set_interact_object(triggerIds=[10000131], state=1)
        set_mesh(triggerIds=[201,202,203], visible=False)
        set_ladder(triggerIds=[301], visible=False, animationEffect=False)
        set_ladder(triggerIds=[302], visible=False, animationEffect=False)
        set_ladder(triggerIds=[303], visible=False, animationEffect=False)
        set_ladder(triggerIds=[304], visible=False, animationEffect=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000131], arg2=0):
            return 발판등장1()


class 발판등장1(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[201], visible=True)
        set_timer(timerId='2', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 발판등장2()


class 발판등장2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[202], visible=True)
        set_timer(timerId='3', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 발판등장3()


class 발판등장3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[203], visible=True)
        set_timer(timerId='4', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 사다리등장()


class 사다리등장(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[301], visible=True, animationEffect=True)
        set_effect(triggerIds=[401], visible=True)
        set_ladder(triggerIds=[302], visible=True, animationEffect=True)
        set_effect(triggerIds=[402], visible=True)
        set_ladder(triggerIds=[303], visible=True, animationEffect=True)
        set_effect(triggerIds=[403], visible=True)
        set_ladder(triggerIds=[304], visible=True, animationEffect=True)
        set_effect(triggerIds=[404], visible=True)
        set_timer(timerId='4', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 대기()


