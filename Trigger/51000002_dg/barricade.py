""" trigger/51000002_dg/barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=False, arg3=0, arg4=0)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[99]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_timer(timerId='90', seconds=90)

    def on_tick(self) -> state.State:
        if time_expired(timerId='90'):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=True, arg3=0, arg4=200)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 차단해제()
        if not user_detected(boxIds=[102]):
            return 대기()


class 차단해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[301], visible=False, arg3=0, arg4=0)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[102]):
            return 대기()


