""" trigger/02000298_bf/mob_06.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            create_monster(spawnIds=[1006], arg2=False)
            return 종료()
        if user_detected(boxIds=[104]):
            create_monster(spawnIds=[1006], arg2=False)
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_timer(timerId='1800000', seconds=1800000)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1800000'):
            return None # Missing State: 종료2


