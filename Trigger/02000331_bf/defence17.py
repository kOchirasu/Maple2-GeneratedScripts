""" trigger/02000331_bf/defence17.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[99993]):
            return 전투시작()


class 전투시작(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=9030, spawnIds=[999]):
            return 전투중()


class 전투중(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[999]):
            return 생존체크01()


class 생존체크01(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=99997, spawnIds=[601]):
            return 생존체크02()
        if monster_dead(boxIds=[601]):
            return 종료()


class 생존체크02(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=99997, spawnIds=[602]):
            return 생존체크03()
        if monster_dead(boxIds=[602]):
            return 종료()


class 생존체크03(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=99997, spawnIds=[603]):
            return 생존체크04()
        if monster_dead(boxIds=[603]):
            return 종료()


class 생존체크04(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=99997, spawnIds=[604]):
            return 생존체크05()
        if monster_dead(boxIds=[604]):
            return 종료()


class 생존체크05(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=99997, spawnIds=[605]):
            return 업적발생()
        if monster_dead(boxIds=[605]):
            return 종료()


class 업적발생(state.State):
    def on_enter(self):
        set_achievement(triggerId=99996, type='trigger', achieve='defence_child') # defence_child


class 종료(state.State):
    pass


