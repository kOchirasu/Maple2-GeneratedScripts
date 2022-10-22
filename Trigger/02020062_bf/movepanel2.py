""" trigger/02020062_bf/movepanel2.xml """
from common import *
import state


class 발판초기화(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], enabled=False)
        set_visible_breakable_object(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], arg2=False)
        set_user_value(triggerId=99990025, key='MovePanel02', value=0)
        set_interact_object(triggerIds=[12000116], state=2) # 이동발판트리거

    def on_tick(self) -> state.State:
        if user_value(key='MovePanel02', value=1):
            return 레버생성()


class 레버생성(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000116], state=1) # 이동발판트리거

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[12000116], arg2=0):
            return 발판이동()


class 발판이동(state.State):
    def on_enter(self):
        set_visible_breakable_object(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], arg2=True)
        set_interact_object(triggerIds=[12000116], state=2) # 이동발판트리거

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9201]):
            set_breakable(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], enabled=True)
            return 대기()
        if user_detected(boxIds=[9204]):
            set_breakable(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], enabled=True)
            return 대기()


class 대기(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9204]):
            set_breakable(triggerIds=[2100,2101,2102,2103,2104,2105,2106,2107,2108], enabled=False)
            return 발판이동()


