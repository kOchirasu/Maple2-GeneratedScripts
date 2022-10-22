""" trigger/52000002_qd/stage03.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000612,10000613,10000614,10000615,10000616], arg2=2):
            return 박스체크()
        if not user_detected(boxIds=[101]):
            return 시작대기중()


class 박스체크(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 안내시작()
        if not user_detected(boxIds=[101]):
            return 시작대기중()


class 안내시작(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25200206, textId=25200206)
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[105]):
            return 종료()
        if not user_detected(boxIds=[101]):
            return 시작대기중()


class 종료(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=25200206)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[101]):
            return 시작대기중()


