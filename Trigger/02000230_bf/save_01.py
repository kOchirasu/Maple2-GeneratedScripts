""" trigger/02000230_bf/save_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[100], arg2=False)
        set_actor(triggerId=101, visible=True, initialSequence='Emotion_Failure_Idle_A')
        set_actor(triggerId=10101, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=10102, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=10103, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=10104, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=10105, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> state.State:
        if true():
            return 주민구출()


class 주민구출(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000354], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000354], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=3)
        set_conversation(type=1, spawnId=100, script='$02000230_BF__SAVE_01__0$', arg4=2, arg5=0)
        set_actor(triggerId=10101, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[10111], arg2=True)
        set_actor(triggerId=10102, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[10112], arg2=True)
        set_actor(triggerId=10103, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[10113], arg2=True)
        set_actor(triggerId=10104, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[10114], arg2=True)
        set_actor(triggerId=10105, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[10115], arg2=True)
        set_conversation(type=1, spawnId=10111, script='$02000230_BF__SAVE_01__1$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=10113, script='$02000230_BF__SAVE_01__2$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 도망과공격()


class 도망과공격(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[100])
        set_actor(triggerId=101, visible=False, initialSequence='Emotion_Failure_Idle_A')
        create_monster(spawnIds=[111], arg2=False)
        set_conversation(type=1, spawnId=111, script='$02000230_BF__SAVE_01__3$', arg4=2, arg5=0)
        move_npc(spawnId=111, patrolName='MS2PatrolData_111_11000687')
        set_conversation(type=1, spawnId=111, script='$02000230_BF__SAVE_01__4$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=90111, spawnIds=[111]):
            return 도망완료()


class 도망완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[111])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[10111,10112,10113,10114,10115]):
            return 트리거초기화()
        if not monster_in_combat(boxIds=[10111,10112,10113,10114,10115]):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=10)
        destroy_monster(spawnIds=[10111,10112,10113,10114,10115])

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 대기()


