""" trigger/99999883/testtrigger4.xml """
from common import *
import state


class START(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001]):
            return idle()


class idle(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True)


