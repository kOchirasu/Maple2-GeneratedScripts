""" trigger/02020062_bf/movepanel3.xml """
from common import *
import state


class 발판초기화(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[2200,2201,2202,2203,2204,2205,2206,2207,2208], enabled=False)
        set_visible_breakable_object(triggerIds=[2200,2201,2202,2203,2204,2205,2206,2207,2208], arg2=False)
        set_user_value(triggerId=99990026, key='MovePanel03', value=0)
        set_interact_object(triggerIds=[12000117], state=2) # 이동발판트리거

    def on_tick(self) -> state.State:
        if user_value(key='MovePanel03', value=1):
            return 레버생성()


class 레버생성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000117], state=1) # 이동발판트리거

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000117], arg2=0):
            return 발판이동()


class 발판이동(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[2200,2201,2202,2203,2204,2205,2206,2207,2208], arg2=True)
        set_interact_object(triggerIds=[12000117], state=2) # 이동발판트리거

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9202]):
            set_breakable(triggerIds=[2200,2201,2202,2203,2204,2205,2206,2207,2208], enabled=True)
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[2200,2201,2202,2203,2204,2205,2206,2207,2208], enabled=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 발판이동()


