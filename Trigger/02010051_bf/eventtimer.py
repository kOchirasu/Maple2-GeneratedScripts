""" trigger/02010051_bf/eventtimer.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9003]):
            return 시간체크()


class 시간체크(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='timercheck', value=1):
            return 업적이벤트()
        if wait_tick(waitTick=240000):
            return 종료()


class 업적이벤트(state.State):
    def on_enter(self):
        set_achievement(triggerId=9003, type='trigger', achieve='CaboTimeEvent')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 업적이벤트()
        if monster_dead(boxIds=[99]):
            return 종료()


class 종료(state.State):
    pass


