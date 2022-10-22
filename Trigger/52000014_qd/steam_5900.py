""" trigger/52000014_qd/steam_5900.xml """
from common import *
import state


class 대기(state.State):
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
        set_timer(timerId='2', seconds=1)
        create_monster(spawnIds=[590], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 발사02()


class 발사02(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)
        create_monster(spawnIds=[591], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 딜레이02()


class 딜레이02(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=1)
        destroy_monster(spawnIds=[590])

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 발사03()


class 발사03(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=2)
        create_monster(spawnIds=[591], arg2=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 초기화()


class 초기화(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[591])

    def on_tick(self) -> state.State:
        if true():
            return 딜레이01()


