""" trigger/02000329_bf/cave.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[711]):
            return 동굴전환시작()


class 동굴전환시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6701], visible=False)


