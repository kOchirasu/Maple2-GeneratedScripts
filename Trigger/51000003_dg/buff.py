""" trigger/51000003_dg/buff.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Tutorial', value=1):
            return Tutorial_buff()


class Tutorial_buff(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Tutorial', value=0):
            return idle()
        if user_detected(boxIds=[701]):
            return buff()


class buff(state.State):
    def on_enter(self):
        add_buff(boxIds=[701], skillId=70000085, level=1, arg5=False) # 무적

    def on_tick(self) -> state.State:
        if user_value(key='Tutorial', value=0):
            return idle()
        if true():
            return Tutorial_buff()


