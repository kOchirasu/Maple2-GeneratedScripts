""" trigger/02000313_bf/regenmob04.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=12, spawnIds=[91]):
            return 소환몹등장()


class 소환몹등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102]):
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 시작대기중()

    def on_exit(self):
        reset_timer(timerId='1')


