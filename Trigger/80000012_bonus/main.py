""" trigger/80000012_bonus/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        select_camera(triggerId=8001, enable=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701]):
            return start()


class start(state.State):
    def on_enter(self):
        create_monster(spawnIds=[199], arg2=False) # 웨이브 장치 작동

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            return end()


class end(state.State):
    pass


