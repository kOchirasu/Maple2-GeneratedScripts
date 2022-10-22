""" trigger/02020062_bf/movepanel4.xml """
from common import *
import state


class 발판초기화(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[2300,2301,2302,2303,2304,2305,2306,2307,2308], enabled=False)
        set_visible_breakable_object(triggerIds=[2300,2301,2302,2303,2304,2305,2306,2307,2308], arg2=False)
        set_user_value(triggerId=99990027, key='MovePanel04', value=0)
        set_interact_object(triggerIds=[12000118], state=2) # 이동발판트리거

    def on_tick(self) -> state.State:
        if user_value(key='MovePanel04', value=1):
            return 레버생성()


class 레버생성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000118], state=1) # 이동발판트리거

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000118], arg2=0):
            return 발판이동()


class 발판이동(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[2300,2301,2302,2303,2304,2305,2306,2307,2308], arg2=True)
        set_interact_object(triggerIds=[12000118], state=2) # 이동발판트리거

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9203]):
            set_breakable(triggerIds=[2300,2301,2302,2303,2304,2305,2306,2307,2308], enabled=True)
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[2300,2301,2302,2303,2304,2305,2306,2307,2308], enabled=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 발판이동()


