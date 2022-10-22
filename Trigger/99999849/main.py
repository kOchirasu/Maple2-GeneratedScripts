""" trigger/99999849/main.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Test', value=2):
            return None # Missing State: 두번


