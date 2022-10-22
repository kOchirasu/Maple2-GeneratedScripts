""" trigger/52000002_qd/stage01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 안내시작()
        if not user_detected(boxIds=[101]):
            return 시작대기중()


class 안내시작(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25200204, textId=25200204)
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000607,10000608,10000609,10000610,10000611], arg2=0):
            return 종료()
        if not user_detected(boxIds=[101]):
            return 시작대기중()


class 종료(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25200204)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[101]):
            return 시작대기중()


