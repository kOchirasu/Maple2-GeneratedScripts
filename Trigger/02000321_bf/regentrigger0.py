""" trigger/02000321_bf/regentrigger0.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=100, spawnIds=[900]):
            return None


class 웜리젠91(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1,2])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1,2]):
            return 웜리젠91쿨타임()


class 웜리젠91쿨타임(state.State):
    def on_enter(self):
        reset_timer(timerId='9')
        set_timer(timerId='9', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='9'):
            reset_timer(timerId='9')
            return 시작대기중()


