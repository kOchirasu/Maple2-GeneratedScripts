""" trigger/52000051_qd/03_removelight.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='ResetInnerLight', value=0)
        set_user_value(key='RemoveInnerLight', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='ResetInnerLight', value=1):
            return Play()


class Play(state.State):
    def on_enter(self):
        set_user_value(key='ResetInnerLight', value=0)
        set_user_value(key='RemoveInnerLight', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='RemoveInnerLight', value=1):
            return RemoveLight01()


class RemoveLight01(state.State):
    def on_enter(self):
        add_buff(boxIds=[9001], skillId=70000103, level=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Wait()


