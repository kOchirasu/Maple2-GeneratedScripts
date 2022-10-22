""" trigger/02000303_bf/object_04.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000601], state=0)
        set_interact_object(triggerIds=[10000602], state=0)
        set_interact_object(triggerIds=[10000603], state=0)
        set_interact_object(triggerIds=[10000604], state=0)
        set_interact_object(triggerIds=[10000605], state=0)
        set_effect(triggerIds=[60601], visible=False)
        set_effect(triggerIds=[60602], visible=False)
        set_effect(triggerIds=[60603], visible=False)
        set_effect(triggerIds=[60604], visible=False)
        set_effect(triggerIds=[60605], visible=False)

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
        set_effect(triggerIds=[60601], visible=True)
        set_interact_object(triggerIds=[10000601], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000601], arg2=0):
            set_effect(triggerIds=[60601], visible=False)
            return 종료()


class 생성02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60602], visible=True)
        set_interact_object(triggerIds=[10000602], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000602], arg2=0):
            set_effect(triggerIds=[60602], visible=False)
            return 종료()


class 생성03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60603], visible=True)
        set_interact_object(triggerIds=[10000603], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000603], arg2=0):
            set_effect(triggerIds=[60603], visible=False)
            return 종료()


class 생성04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60604], visible=True)
        set_interact_object(triggerIds=[10000604], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000604], arg2=0):
            set_effect(triggerIds=[60604], visible=False)
            return 종료()


class 생성05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60605], visible=True)
        set_interact_object(triggerIds=[10000605], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000605], arg2=0):
            set_effect(triggerIds=[60605], visible=False)
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='120', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='120'):
            return 생성랜덤()


