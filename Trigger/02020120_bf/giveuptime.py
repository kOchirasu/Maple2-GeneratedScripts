""" trigger/02020120_bf/giveuptime.xml """
from common import *
import state


#  이 트리거 사용 안함
class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 타이머()


class 타이머(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 종료()


class 종료(state.State):
    pass


