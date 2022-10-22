""" trigger/52010018_qd/main_3.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[1001], arg2=False)
        create_monster(spawnIds=[1005], arg2=False)

    def on_tick(self) -> state.State:
        if true():
            return 분기점()


class 분기점(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[100], questIds=[10002851], questStates=[2]):
            destroy_monster(spawnIds=[1005])
            return 종료()
        if quest_user_detected(boxIds=[100], questIds=[10002852], questStates=[1]):
            destroy_monster(spawnIds=[1005])
            return 종료()
        if quest_user_detected(boxIds=[100], questIds=[10002853], questStates=[1]):
            destroy_monster(spawnIds=[1005])
            return 종료()
        if quest_user_detected(boxIds=[100], questIds=[10002853], questStates=[2]):
            destroy_monster(spawnIds=[1005])
            return 종료()
        if quest_user_detected(boxIds=[100], questIds=[10002851], questStates=[3]):
            return 분기점2()


class 분기점2(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[100], questIds=[10002852], questStates=[2]):
            return 종료()
        if quest_user_detected(boxIds=[100], questIds=[10002852], questStates=[3]):
            return 종료()
        if not quest_user_detected(boxIds=[100], questIds=[10002852], questStates=[2]):
            destroy_monster(spawnIds=[1005])
            return 종료()


class 종료(state.State):
    pass


