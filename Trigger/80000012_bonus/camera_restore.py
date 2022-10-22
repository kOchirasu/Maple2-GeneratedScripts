""" trigger/80000012_bonus/camera_restore.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=True)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return camera_restore()


class camera_restore(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=True)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return idle()


