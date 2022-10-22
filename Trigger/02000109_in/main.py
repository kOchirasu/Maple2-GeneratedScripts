""" trigger/02000109_in/main.xml """
from common import *
import state


class start(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4001,4002,4003,4004], visible=True)
        set_mesh(triggerIds=[4011], visible=False)
        destroy_monster(spawnIds=[101,102])

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return 퀘스트조건체크()


class 퀘스트조건체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[3]):
            return 종료()
        if quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[2]):
            return 일기장스폰_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[1]):
            return 일기장스폰_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 일기장스폰_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 벽삭제()
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[3]):
            return npc스폰_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[2]):
            return npc스폰_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[1]):
            return 종료()


class 퀘스트진행체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[3]):
            return 종료()
        if quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[2]):
            return None # Missing State: 일기장스폰
        if quest_user_detected(boxIds=[9000], questIds=[50001608], questStates=[1]):
            return None # Missing State: 일기장스폰
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return None # Missing State: 일기장스폰
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰_대기()
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 벽삭제()
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[3]):
            return npc스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[2]):
            return npc스폰()
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[1]):
            return 종료()


class npc스폰_대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 벽삭제()
        if not quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 퀘스트진행체크()


class npc스폰(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 벽삭제()
        if not quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[1]):
            return 퀘스트진행체크()


class 벽삭제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰_대기()
        if not quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 퀘스트진행체크()


class 일기장스폰_대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)
        set_mesh(triggerIds=[4011], visible=True)
        set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 종료()
        if not quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 일기장스폰01()


class 일기장스폰01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4011], visible=True)
        set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 종료()
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰02()
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[3]):
            return 일기장없어짐()
        if not quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 일기장스폰02()


class 일기장스폰02(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[4011], visible=True)
        set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 종료()
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰01()
        if quest_user_detected(boxIds=[9000], questIds=[50001606], questStates=[3]):
            return 일기장없어짐()
        if not quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[3]):
            return 일기장스폰01()


class 일기장없어짐(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        set_mesh(triggerIds=[4011], visible=False)
        set_mesh(triggerIds=[4001,4002,4003,4004], visible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 일기장스폰_대기()
        if not quest_user_detected(boxIds=[9000], questIds=[50001607], questStates=[2]):
            return 퀘스트진행체크()


class 종료(state.State):
    pass


