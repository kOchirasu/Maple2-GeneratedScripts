""" trigger/52000025_qd/talk_event.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702]):
            return talk_01()


class talk_01(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='$52000025_QD__TALK_EVENT__0$', arg4=3, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return talk_02()


class talk_02(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='$52000025_QD__TALK_EVENT__1$', arg4=2, arg5=1)


