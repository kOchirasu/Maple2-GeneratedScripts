""" trigger/02000148_bf/01_trigger03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000171], state=1)
        set_effect(triggerIds=[209,210,211,212], visible=False)
        set_mesh(triggerIds=[317,318,319,320], visible=True)
        set_mesh(triggerIds=[321,322,323,324], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000171], arg2=0):
            return 개봉박두()


class 개봉박두(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[317,318,319,320], visible=False)
        create_monster(spawnIds=[99,100,101,102], arg2=True)
        set_mesh(triggerIds=[321,322,323,324], visible=True)
        set_effect(triggerIds=[209,210,211,212], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99,100,101,102]):
            return 유저감지()


class 유저감지(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[403]):
            return 대기()


