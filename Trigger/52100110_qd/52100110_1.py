""" trigger/52100110_qd/52100110_1.xml """
from common import *
import state


class Ready521001101(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1000]):
            return 화이트박스생성521001101()
        if user_detected(boxIds=[2000]):
            return 화이트박스생성521001101()


class 화이트박스생성521001101(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        set_mesh(triggerIds=[10000], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트체크521001101()


class 퀘스트체크521001101(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2000], questIds=[50101040], questStates=[1]):
            return 화이트박스제거521001101()


class 화이트박스제거521001101(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10000], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: 


