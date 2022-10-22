""" trigger/52100110_qd/52100110.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10000], visible=False)
        set_effect(triggerIds=[601], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1000]):
            return 퀘스트체크()


class 퀘스트체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1000], questIds=[50101040], questStates=[1]):
            return 화이트박스제거()
        if quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[3]):
            return 로텔레포트52100105()
        if quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[2]):
            return 퀘스트용몬스터스폰()
        if quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[1]):
            return 퀘스트용몬스터스폰()
        if quest_user_detected(boxIds=[1000], questIds=[50101020], questStates=[3]):
            return 퀘스트용몬스터스폰()


class 퀘스트체크2(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1000], questIds=[50101040], questStates=[1]):
            return 화이트박스제거()
        if quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[3]):
            return None # Missing State: 


class 로텔레포트52100105(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10000], visible=True)
        move_user(mapId=52100105, portalId=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: 


class 퀘스트용몬스터스폰(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102,103], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 화이트박스생성2()


class 화이트박스생성2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10000], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 퀘스트체크2()


class 화이트박스제거(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[10000], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: 

