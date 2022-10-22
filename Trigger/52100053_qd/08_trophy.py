""" trigger/52100053_qd/08_trophy.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9900]):
            return 룸체크()


class 룸체크(state.State):
    def on_tick(self) -> state.State:
        if is_dungeon_room():
            return 트로피지급()


class 트로피지급(state.State):
    def on_enter(self):
        set_achievement(triggerId=9900, type='trigger', achieve='Find02000397')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 대기()


