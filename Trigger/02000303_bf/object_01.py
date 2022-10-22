""" trigger/02000303_bf/object_01.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000586], state=0)
        set_interact_object(triggerIds=[10000587], state=0)
        set_interact_object(triggerIds=[10000588], state=0)
        set_interact_object(triggerIds=[10000589], state=0)
        set_interact_object(triggerIds=[10000590], state=0)
        set_effect(triggerIds=[60586], visible=False)
        set_effect(triggerIds=[60587], visible=False)
        set_effect(triggerIds=[60588], visible=False)
        set_effect(triggerIds=[60589], visible=False)
        set_effect(triggerIds=[60590], visible=False)

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
        set_effect(triggerIds=[60586], visible=True)
        set_interact_object(triggerIds=[10000586], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000586], arg2=0):
            set_effect(triggerIds=[60586], visible=False)
            return 종료()


class 생성02(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000587], state=1)
        set_effect(triggerIds=[60587], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000587], arg2=0):
            set_effect(triggerIds=[60587], visible=False)
            return 종료()


class 생성03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60588], visible=True)
        set_interact_object(triggerIds=[10000588], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000588], arg2=0):
            set_effect(triggerIds=[60588], visible=False)
            return 종료()


class 생성04(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60589], visible=True)
        set_interact_object(triggerIds=[10000589], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000589], arg2=0):
            set_effect(triggerIds=[60589], visible=False)
            return 종료()


class 생성05(state.State):
    def on_enter(self):
        set_effect(triggerIds=[60590], visible=True)
        set_interact_object(triggerIds=[10000590], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000590], arg2=0):
            set_effect(triggerIds=[60590], visible=False)
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='120', seconds=120)

    def on_tick(self) -> state.State:
        if time_expired(timerId='120'):
            return 생성랜덤()


