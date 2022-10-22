""" trigger/61000010_me/winner.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 업적()


class 업적(state.State):
    def on_enter(self):
        set_achievement(triggerId=102, type='trigger', achieve='WinSanghaiRunners')


