""" trigger/02000525_bf/barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348], visible=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=11, spawnIds=[101]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348], visible=True, arg3=0, arg4=200)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 차단해제()
        if not user_detected(boxIds=[11]):
            return 대기()


class 차단해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348], visible=False, arg3=0, arg4=200)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[11]):
            return 대기()


