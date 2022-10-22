""" trigger/61000011_me/wait.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 종료()


class 종료(state.State):
    pass


