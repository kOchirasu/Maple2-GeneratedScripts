""" trigger/99999925/checkpolymorph.xml """
from common import *
import state


class CheckIdle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='BuffGo', value=1):
            return Checkpoly()


class Checkpoly(state.State):
    def on_enter(self):
        set_ai_extra_data(key='BuffStart', value=1, isModify=True)
        set_user_value(key='BuffGo', value=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return CheckIdle()


