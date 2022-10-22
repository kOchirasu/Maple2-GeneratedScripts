""" trigger/02020098_bf/message.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[11]):
            return 크리스탈활용안내메시지출력()


class 크리스탈활용안내메시지출력(state.State):
    def on_enter(self):
        show_guide_summary(entityId=29200002, textId=29200002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6300):
            return 트리거종료()

    def on_exit(self):
        hide_guide_summary(entityId=29200002)


class 트리거종료(state.State):
    pass


