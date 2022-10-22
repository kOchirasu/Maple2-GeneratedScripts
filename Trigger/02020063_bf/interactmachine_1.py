""" trigger/02020063_bf/interactmachine_1.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9001]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002141], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002141], arg2=0):
            return 재활성대기()


class 재활성대기(state.State):
    def on_tick(self) -> state.State:
        if not check_any_user_additional_effect(boxId=9101, additionalEffectId=99910370, level=1):
            return 시작()


class 종료(state.State):
    pass

