""" trigger/61000012_me/main.xml """
from common import *
import state


class 입장(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료()


class 종료(state.State):
    pass


