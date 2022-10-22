""" trigger/02000319_bf/barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112], visible=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=202, spawnIds=[301]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=1200)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112], visible=True, arg3=0, arg4=200)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[301]):
            return 차단해제()
        if not user_detected(boxIds=[202]):
            return 대기()


class 차단해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112], visible=False, arg3=0, arg4=200)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[202]):
            return 대기()


