""" trigger/02000146_bf/ia_112.xml """
from common import *
import state


class 시작대기중(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000187], state=1)
        set_actor(triggerId=212, visible=True, initialSequence='Attack_Idle_A')

    def on_tick(self) -> state.State:
        if true():
            return 오브젝트반응()


class 오브젝트반응(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000187], arg2=0):
            return NPC등장()

    def on_exit(self):
        set_actor(triggerId=212, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[412])


class NPC등장(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=412, script='$02000146_BF__IA_112__0$', arg4=2)
        set_timer(timerId='1', seconds=15)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[412]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=8)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 시작대기중()


