""" trigger/02000049_bf/trigger_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])
        set_interact_object(triggerIds=[10000286], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000286], arg2=0):
            return 반항()


class 반항(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=True)
        set_conversation(type=1, spawnId=201, script='$02000049_BF__TRIGGER_02__0$', arg4=2)

    def on_tick(self) -> state.State:
        if true():
            return 반항2()


class 반항2(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30, clearAtZero=False)
        set_interact_object(triggerIds=[10000286], state=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


