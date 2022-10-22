""" trigger/02020100_bf/seed1.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990001, key='Seed1interact', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='Seed1start', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1302], visible=True, arg3=0, arg4=0, arg5=2)
        set_interact_object(triggerIds=[10002109], state=1, arg3=True)

    def on_tick(self) -> state.State:
        if user_value(key='Seed1start', value=2):
            return 종료()
        if object_interacted(interactIds=[10002109], arg2=0):
            return 씨앗1_대기()


class 씨앗1_대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1302], visible=False, arg3=0, arg4=0, arg5=0)
        set_interact_object(triggerIds=[10002109], state=0, arg3=True)
        set_user_value(triggerId=99990001, key='Seed1interact', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='Seed1start', value=2):
            return 종료()
        if not check_any_user_additional_effect(boxId=0, additionalEffectId=70002109, level=1):
            return 시작()


class 종료(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002109], state=0)


