""" trigger/03000049_bf/trigger_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])
        set_interact_object(triggerIds=[10000288], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000288], arg2=0):
            return 반항()


class 반항(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True)
        set_conversation(type=1, spawnId=202, script='$03000049_BF__TRIGGER_03__0$', arg4=2)

    def on_tick(self) -> state.State:
        if true():
            return 반항2()


class 반항2(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=30, clearAtZero=False)
        set_interact_object(triggerIds=[10000288], state=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()

