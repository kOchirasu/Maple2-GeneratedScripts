""" trigger/52000063_qd/random_skill_b.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[606], visible=False)

    def on_tick(self) -> state.State:
        if user_value(key='gameStart', value=1):
            return 감지대기()


class 감지대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=True)
        set_effect(triggerIds=[605], visible=True)
        set_effect(triggerIds=[606], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[112]):
            return 스킬랜덤()


class 스킬랜덤(state.State):
    def on_enter(self):
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[606], visible=False)

    def on_tick(self) -> state.State:
        if random_condition(rate=80):
            add_buff(boxIds=[199], skillId=70000008, level=1, arg4=False, arg5=False)
            return 종료()
        if random_condition(rate=20):
            add_buff(boxIds=[199], skillId=70000009, level=1, arg4=False, arg5=False)
            return 종료()


class 종료(state.State):
    pass


