""" trigger/03000087_bf/slime.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return 알림()


class 알림(state.State):
    def on_enter(self):
        show_guide_summary(entityId=23000005, textId=23000005, duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 알림()


class 종료(state.State):
    pass


