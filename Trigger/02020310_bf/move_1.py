""" trigger/02020310_bf/move_1.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Archeon1', value=1):
            set_user_value(triggerId=900007, key='Archeon1', value=0)
            return Archeon_Ready()


class Archeon_Ready(state.State):
    def on_tick(self) -> state.State:
        if check_any_user_additional_effect(boxId=10001, additionalEffectId=73000005, level=1):
            move_user_to_pos(pos=[8700,-4800,2750], rot=[0,0,0])
            return Archeon_On()


class Archeon_On(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대기()


