""" trigger/02000230_bf/save_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[200], arg2=False)
        set_actor(triggerId=201, visible=True, initialSequence='Emotion_Failure_Idle_A')
        set_actor(triggerId=20201, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=20202, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=20203, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=20204, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=20205, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> state.State:
        if true():
            return 주민구출()


class 주민구출(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000279], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000279], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=3)
        set_conversation(type=1, spawnId=200, script='$02000230_BF__SAVE_02__0$', arg4=2, arg5=0)
        set_actor(triggerId=20201, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[20211], arg2=True)
        set_actor(triggerId=20202, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[20212], arg2=True)
        set_actor(triggerId=20203, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[20213], arg2=True)
        set_actor(triggerId=20204, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[20214], arg2=True)
        set_actor(triggerId=20205, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[20215], arg2=True)
        set_conversation(type=1, spawnId=20211, script='$02000230_BF__SAVE_02__1$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=20213, script='$02000230_BF__SAVE_02__2$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 도망과공격()


class 도망과공격(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[200])
        set_actor(triggerId=201, visible=False, initialSequence='Emotion_Failure_Idle_A')
        create_monster(spawnIds=[211], arg2=False)
        set_conversation(type=1, spawnId=211, script='$02000230_BF__SAVE_02__3$', arg4=2, arg5=0)
        move_npc(spawnId=211, patrolName='MS2PatrolData_211_11000688')
        set_conversation(type=1, spawnId=211, script='$02000230_BF__SAVE_02__4$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=90211, spawnIds=[211]):
            return 도망완료()


class 도망완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[211])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[20211,20212,20213,20214,20215]):
            return 트리거초기화()
        if not monster_in_combat(boxIds=[20211,20212,20213,20214,20215]):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=10)
        destroy_monster(spawnIds=[20211,20212,20213,20214,20215])

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 대기()


