""" trigger/02000471_bf/interactcheck.xml """
from common import *
import state


class check(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040314, key='InteractClear', value=0)

    def on_tick(self) -> state.State:
        if all_of():
            return clear()


class clear(state.State):
    def on_enter(self):
        set_user_value(triggerId=2040314, key='InteractClear', value=1)
        set_user_value(triggerId=2040322, key='InteractClear', value=1)


