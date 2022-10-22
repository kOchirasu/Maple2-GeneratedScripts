""" trigger/66000004_gd/cannon.xml """
from common import *
import state


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 대포등장()


class 대포등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001,1002,1003,1004], arg2=False)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[104]):
            return 소환해제()


class 소환해제(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[1001,1002,1003,1004], arg2=False)


