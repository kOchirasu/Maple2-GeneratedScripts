""" trigger/02000303_bf/object_02.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000591], state=0)
        set_interact_object(triggerIds=[10000592], state=0)
        set_interact_object(triggerIds=[10000593], state=0)
        set_interact_object(triggerIds=[10000594], state=0)
        set_interact_object(triggerIds=[10000595], state=0)
        set_effect(triggerIds=[60591], visible=False)
        set_effect(triggerIds=[60592], visible=False)
        set_effect(triggerIds=[60593], visible=False)
        set_effect(triggerIds=[60594], visible=False)
        set_effect(triggerIds=[60595], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 생성랜덤()


class 생성랜덤(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=20):
            return 생성01()
        if random_condition(rate=20):
            return 생성02()
        if random_condition(rate=20):
            return 생성03()
        if random_condition(rate=20):
            return 생성04()
        if random_condition(rate=20):
            return 생성05()


class 생성01(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000591], state=1)
        set_effect(triggerIds=[60591], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000591], arg2=0):
            set_effect(triggerIds=[60591], visible=False)
            return 종료()


class 생성02(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000592], state=1)
        set_effect(triggerIds=[60592], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000592], arg2=0):
            set_effect(triggerIds=[60592], visible=False)
            return 종료()


class 생성03(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000593], state=1)
        set_effect(triggerIds=[60593], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000593], arg2=0):
            set_effect(triggerIds=[60593], visible=False)
            return 종료()


class 생성04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60594], visible=True)
        set_interact_object(triggerIds=[10000594], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000594], arg2=0):
            set_effect(triggerIds=[60594], visible=False)
            return 종료()


class 생성05(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000595], state=1)
        set_effect(triggerIds=[60595], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000595], arg2=0):
            set_effect(triggerIds=[60595], visible=False)
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='120', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='120'):
            return 생성랜덤()


