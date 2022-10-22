""" trigger/02000428_bf/airshipbalrogcrimsonflamekillplayer.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=750, boxId=1):
            return 전투시작()


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if dungeon_check_play_time(playSeconds=540):
            return 종료()


class 종료(state.State):
    pass


