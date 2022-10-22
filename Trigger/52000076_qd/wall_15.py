""" trigger/52000076_qd/wall_15.xml """
from common import *
import state


class 벽재생(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31501,31502,31503,31504,31505,31506,31507,31508,31509,31510,31511,31512,31513,31514,31515,31516,31517,31518,31519,31520], visible=True, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[115]):
            return 벽삭제()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[31501,31502,31503,31504,31505,31506,31507,31508,31509,31510,31511,31512,31513,31514,31515,31516,31517,31518,31519,31520], visible=False, arg3=0, arg4=10, arg5=3)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[115]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 벽재생()


