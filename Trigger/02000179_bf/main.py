""" trigger/02000179_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return None # Missing State: 퀘스트조건체크


class 종료(state.State):
    pass


