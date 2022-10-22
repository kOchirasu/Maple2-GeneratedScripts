""" trigger/52000014_qd/steam_5400.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 발사01()


class 발사01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        create_monster(spawnIds=[540], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 초기화()


class 초기화(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[540])

    def on_tick(self) -> state.State:
        if true():
            return 발사01()


