""" trigger/02000230_bf/save_05.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[500], arg2=False)
        set_actor(triggerId=501, visible=True, initialSequence='Emotion_Failure_Idle_A')
        set_actor(triggerId=50501, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=50502, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=50503, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=50504, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=50505, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> state.State:
        if true():
            return 주민구출()


class 주민구출(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000357], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000357], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=3)
        set_conversation(type=1, spawnId=500, script='$02000230_BF__SAVE_05__0$', arg4=2, arg5=0)
        set_actor(triggerId=50501, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[50511], arg2=True)
        set_actor(triggerId=50502, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[50512], arg2=True)
        set_actor(triggerId=50503, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[50513], arg2=True)
        set_actor(triggerId=50504, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[50514], arg2=True)
        set_actor(triggerId=50505, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[50515], arg2=True)
        set_conversation(type=1, spawnId=50511, script='$02000230_BF__SAVE_05__1$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=50513, script='$02000230_BF__SAVE_05__2$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 도망과공격()


class 도망과공격(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[500])
        set_actor(triggerId=501, visible=False, initialSequence='Emotion_Failure_Idle_A')
        create_monster(spawnIds=[511], arg2=False)
        set_conversation(type=1, spawnId=511, script='$02000230_BF__SAVE_05__3$', arg4=2, arg5=0)
        move_npc(spawnId=511, patrolName='MS2PatrolData_511_11000689')
        set_conversation(type=1, spawnId=511, script='$02000230_BF__SAVE_05__4$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=90511, spawnIds=[511]):
            return 도망완료()


class 도망완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[511])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[50511,50512,50513,50514,50515]):
            return 트리거초기화()
        if not monster_in_combat(boxIds=[50511,50512,50513,50514,50515]):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=10)
        destroy_monster(spawnIds=[50511,50512,50513,50514,50515])

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 대기()


