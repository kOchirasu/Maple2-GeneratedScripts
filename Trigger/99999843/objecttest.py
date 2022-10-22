""" trigger/99999843/objecttest.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[12000401], state=1)
        set_interact_object(triggerIds=[12000400], state=2)
        set_interact_object(triggerIds=[12000402], state=2)
        set_interact_object(triggerIds=[12000403], state=2)

    def on_tick(self) -> state.State:
        if all_of():
            return PC_MOVE_01()


class PC_MOVE_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            patrol_condition_user(patrolName='MS2PatrolData0', patrolIndex=1, additionalEffectId=73000006)
            return PC_MOVE_02_Delay()


class PC_MOVE_02_Delay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return PC_MOVE_02()


class PC_MOVE_02(state.State):
    def on_enter(self):
        add_buff(boxIds=[901], skillId=73000009, level=1, arg4=False, arg5=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return PC_MOVE_02_Delay()


class RESET_DELAY(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대기()


