""" trigger/02000230_bf/save_06.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[600], arg2=False)
        set_actor(triggerId=601, visible=True, initialSequence='Emotion_Failure_Idle_A')
        set_actor(triggerId=60601, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=60602, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=60603, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=60604, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=60605, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> state.State:
        if true():
            return 주민구출()


class 주민구출(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000358], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000358], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=3)
        set_conversation(type=1, spawnId=600, script='$02000230_BF__SAVE_06__0$', arg4=2, arg5=0)
        set_actor(triggerId=60601, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[60611], arg2=True)
        set_actor(triggerId=60602, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[60612], arg2=True)
        set_actor(triggerId=60603, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[60613], arg2=True)
        set_actor(triggerId=60604, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[60614], arg2=True)
        set_actor(triggerId=60605, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[60615], arg2=True)
        set_conversation(type=1, spawnId=60611, script='$02000230_BF__SAVE_06__1$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=60613, script='$02000230_BF__SAVE_06__2$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 도망과공격()


class 도망과공격(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[600])
        set_actor(triggerId=601, visible=False, initialSequence='Emotion_Failure_Idle_A')
        create_monster(spawnIds=[611], arg2=False)
        set_conversation(type=1, spawnId=611, script='$02000230_BF__SAVE_06__3$', arg4=2, arg5=0)
        move_npc(spawnId=611, patrolName='MS2PatrolData_611_11000688')
        set_conversation(type=1, spawnId=611, script='$02000230_BF__SAVE_06__4$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=90611, spawnIds=[611]):
            return 도망완료()


class 도망완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[611])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[60611,60612,60613,60614,60615]):
            return 트리거초기화()
        if not monster_in_combat(boxIds=[60611,60612,60613,60614,60615]):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=10)
        destroy_monster(spawnIds=[60611,60612,60613,60614,60615])

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 대기()


