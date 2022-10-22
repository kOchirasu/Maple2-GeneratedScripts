""" trigger/02000041_bf/elite.xml """
from common import *
import state


class 생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1001,1002]):
            return 대기()


class 대기(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30, clearAtZero=False, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='30'):
            return 생성()


