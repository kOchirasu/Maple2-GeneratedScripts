""" trigger/02000303_bf/object_03.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000596], state=0)
        set_interact_object(triggerIds=[10000597], state=0)
        set_interact_object(triggerIds=[10000598], state=0)
        set_interact_object(triggerIds=[10000599], state=0)
        set_interact_object(triggerIds=[10000600], state=0)
        set_effect(triggerIds=[60596], visible=False)
        set_effect(triggerIds=[60597], visible=False)
        set_effect(triggerIds=[60598], visible=False)
        set_effect(triggerIds=[60599], visible=False)
        set_effect(triggerIds=[60600], visible=False)

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
        set_effect(triggerIds=[60596], visible=True)
        set_interact_object(triggerIds=[10000596], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000596], arg2=0):
            set_effect(triggerIds=[60596], visible=False)
            return 종료()


class 생성02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60597], visible=True)
        set_interact_object(triggerIds=[10000597], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000597], arg2=0):
            set_effect(triggerIds=[60597], visible=False)
            return 종료()


class 생성03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60598], visible=True)
        set_interact_object(triggerIds=[10000598], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000598], arg2=0):
            set_effect(triggerIds=[60598], visible=False)
            return 종료()


class 생성04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60599], visible=True)
        set_interact_object(triggerIds=[10000599], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000599], arg2=0):
            set_effect(triggerIds=[60599], visible=False)
            return 종료()


class 생성05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60600], visible=True)
        set_interact_object(triggerIds=[10000600], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000600], arg2=0):
            set_effect(triggerIds=[60600], visible=False)
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='120', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='120'):
            return 생성랜덤()


