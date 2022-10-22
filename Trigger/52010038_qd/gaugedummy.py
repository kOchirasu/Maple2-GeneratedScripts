""" trigger/52010038_qd/gaugedummy.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='GaugeStart', value=1):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[4000], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 생성()
        if user_value(key='GaugeClosed', value=1):
            return 종료()


class 종료(state.State):
    pass


