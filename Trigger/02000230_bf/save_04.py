""" trigger/02000230_bf/save_04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[400], arg2=False)
        set_actor(triggerId=401, visible=True, initialSequence='Emotion_Failure_Idle_A')
        set_actor(triggerId=40401, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=40402, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=40403, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=40404, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=40405, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> state.State:
        if true():
            return 주민구출()


class 주민구출(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000356], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000356], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=3)
        set_conversation(type=1, spawnId=400, script='$02000230_BF__SAVE_04__0$', arg4=2, arg5=0)
        set_actor(triggerId=40401, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[40411], arg2=True)
        set_actor(triggerId=40402, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[40412], arg2=True)
        set_actor(triggerId=40403, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[40413], arg2=True)
        set_actor(triggerId=40404, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[40414], arg2=True)
        set_actor(triggerId=40405, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[40415], arg2=True)
        set_conversation(type=1, spawnId=40411, script='$02000230_BF__SAVE_04__1$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=40413, script='$02000230_BF__SAVE_04__2$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 도망과공격()


class 도망과공격(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[400])
        set_actor(triggerId=401, visible=False, initialSequence='Emotion_Failure_Idle_A')
        create_monster(spawnIds=[411], arg2=False)
        set_conversation(type=1, spawnId=411, script='$02000230_BF__SAVE_04__3$', arg4=2, arg5=0)
        move_npc(spawnId=411, patrolName='MS2PatrolData_411_11000687')
        set_conversation(type=1, spawnId=411, script='$02000230_BF__SAVE_04__4$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=90411, spawnIds=[411]):
            return 도망완료()


class 도망완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[411])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[40411,40412,40413,40414,40415]):
            return 트리거초기화()
        if not monster_in_combat(boxIds=[40411,40412,40413,40414,40415]):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=10)
        destroy_monster(spawnIds=[40411,40412,40413,40414,40415])

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 대기()


