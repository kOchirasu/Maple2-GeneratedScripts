""" trigger/52000014_qd/steam_5000.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[501], arg2=False)
        create_monster(spawnIds=[502], arg2=False)
        create_monster(spawnIds=[503], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 딜레이01()


class 딜레이01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 발사01()


class 발사01(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)
        create_monster(spawnIds=[500], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 초기화()


class 초기화(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[500])

    def on_tick(self) -> state.State:
        if true():
            return 딜레이01()


