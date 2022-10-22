""" trigger/02000148_bf/01_trigger02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000170], state=1)
        set_effect(triggerIds=[205,206,207,208], visible=False)
        set_mesh(triggerIds=[309,310,311,312], visible=True)
        set_mesh(triggerIds=[313,314,315,316], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000170], arg2=0):
            return 개봉박두()


class 개봉박두(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[309,310,311,312], visible=False)
        create_monster(spawnIds=[95,96,97,98], arg2=True)
        set_mesh(triggerIds=[313,314,315,316], visible=True)
        set_effect(triggerIds=[205,206,207,208], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[95,96,97,98]):
            return 유저감지()


class 유저감지(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[402]):
            return 대기()


