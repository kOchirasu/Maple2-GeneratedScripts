""" trigger/52000056_qd/guide.xml """
from common import *
import state


class 가이드(state.State):
    def on_enter(self):
        show_guide_summary(entityId=10010001, textId=10010001)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103,104,105,106]):
            return 종료()
        if wait_tick(waitTick=3000):
            return 가이드()

    def on_exit(self):
        hide_guide_summary(entityId=10010001)


class 종료(state.State):
    pass


