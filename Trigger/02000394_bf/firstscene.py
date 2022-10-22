""" trigger/02000394_bf/firstscene.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            return 카메라연출01()


class 카메라연출01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=3000, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라연출02()


class 카메라연출02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[3000,3001,3002,3003], returnView=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 종료()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0.6)


class 종료(state.State):
    pass


