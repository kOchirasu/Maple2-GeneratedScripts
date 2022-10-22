""" trigger/02000471_bf/elite_06.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return spawn()


class spawn(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Buff', value=1):
            return buff()


class buff(state.State):
    def on_enter(self):
        add_buff(boxIds=[1999], skillId=70002051, level=1, arg4=True, arg5=False)
        add_buff(boxIds=[306], skillId=70002051, level=1, arg4=True, arg5=False)


