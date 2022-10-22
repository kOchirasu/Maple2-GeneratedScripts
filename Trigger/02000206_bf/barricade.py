""" trigger/02000206_bf/barricade.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516], visible=False, arg3=0, arg4=0)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=402, spawnIds=[101]):
            return 카운트()


class 카운트(state.State):
    def on_enter(self):
        set_timer(timerId='5', seconds=50)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return 차단()


class 차단(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516], visible=True, arg3=0, arg4=200)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101]):
            return 차단해제()
        if not user_detected(boxIds=[402]):
            return 대기()


class 차단해제(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516], visible=False, arg3=0, arg4=200)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[402]):
            return 대기()


