""" trigger/02020301_bf/3000055_phase_4_camera_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        select_camera(triggerId=690000, enable=False)

    def on_tick(self) -> state.State:
        if user_value(key='Phase_4_Camera_01', value=1):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        select_camera(triggerId=690000, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 리셋()


class 리셋(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='Phase_4_Camera_01', value=0):
            return 대기()


