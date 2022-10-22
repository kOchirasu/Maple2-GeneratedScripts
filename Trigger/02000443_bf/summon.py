""" trigger/02000443_bf/summon.xml """
from common import *
import state


class special_1_1(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='special_1', value=1):
            return special_1_2()


class special_1_2(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return special_2_1()


class special_2_1(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=False)

    def on_tick(self) -> state.State:
        if user_value(key='special_2', value=1):
            return special_2_2()


class special_2_2(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return special_3_1()


class special_3_1(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=False)

    def on_tick(self) -> state.State:
        if user_value(key='special_3', value=1):
            return special_3_2()


class special_3_2(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return special_4_1()


class special_4_1(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=False)

    def on_tick(self) -> state.State:
        if user_value(key='special_4', value=1):
            return special_4_2()


class special_4_2(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return special_5_1()


class special_5_1(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=False)

    def on_tick(self) -> state.State:
        if user_value(key='special_5', value=1):
            return special_5_2()


class special_5_2(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return end()


class end(state.State):
    def on_enter(self):
        set_local_camera(cameraId=8001, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return None


