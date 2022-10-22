""" trigger/02000213_bf/barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515], visible=False, arg3=0, arg4=0, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[1099]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515], visible=True, arg3=0, arg4=200, arg5=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[1099]):
            return 차단해제()


class 차단해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515], visible=False, arg3=0, arg4=200, arg5=2)


