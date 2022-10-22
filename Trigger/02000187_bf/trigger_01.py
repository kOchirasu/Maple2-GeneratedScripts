""" trigger/02000187_bf/trigger_01.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[101], questIds=[20001281], questStates=[2]):
            return 몹리젠()


class 몹리젠(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201,202,203,204,205,206])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201,202,203,204,205,206]):
            return 쿨타임()


class 쿨타임(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()


