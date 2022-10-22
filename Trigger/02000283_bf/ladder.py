""" trigger/02000283_bf/ladder.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[511], visible=False, animationEffect=False)
        set_ladder(triggerIds=[512], visible=False, animationEffect=False)
        set_ladder(triggerIds=[513], visible=False, animationEffect=False)
        set_ladder(triggerIds=[514], visible=False, animationEffect=False)
        set_interact_object(triggerIds=[10000429], state=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=102, spawnIds=[2001]):
            return 반응대기()


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000429], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000429], arg2=0):
            return 사다리생성()


class 사다리생성(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[511], visible=True, animationEffect=True)
        set_ladder(triggerIds=[512], visible=True, animationEffect=True)
        set_ladder(triggerIds=[513], visible=True, animationEffect=True)
        set_ladder(triggerIds=[514], visible=True, animationEffect=True)
        set_timer(timerId='10', seconds=10, clearAtZero=False, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 종료()


class 종료(state.State):
    pass


