""" trigger/99999925/ladder03.xml """
from common import *
import state


class ladderIdle(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001079], arg2=0):
            return ladderWolk()


class ladderWolk(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[703], visible=False, arg3=1)
        set_ai_extra_data(key='LadderCnt', value=1, isModify=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ladderEnd()


class ladderEnd(state.State):
    pass


