""" trigger/52100023_qd/52100023.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[4000], enabled=False)
        set_visible_breakable_object(triggerIds=[4000], arg2=False)
        create_monster(spawnIds=[1101], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 연출시작()


class 연출시작(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 종료()


class 종료(state.State):
    pass


