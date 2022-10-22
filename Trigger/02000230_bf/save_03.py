""" trigger/02000230_bf/save_03.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[300], arg2=False)
        set_actor(triggerId=301, visible=True, initialSequence='Emotion_Failure_Idle_A')
        set_actor(triggerId=30301, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=30302, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=30303, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=30304, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=30305, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> state.State:
        if true():
            return 주민구출()


class 주민구출(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000355], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000355], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=3)
        set_conversation(type=1, spawnId=300, script='$02000230_BF__SAVE_03__0$', arg4=2, arg5=0)
        set_actor(triggerId=30301, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[30311], arg2=True)
        set_actor(triggerId=30302, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[30312], arg2=True)
        set_actor(triggerId=30303, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[30313], arg2=True)
        set_actor(triggerId=30304, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[30314], arg2=True)
        set_actor(triggerId=30305, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[30315], arg2=True)
        set_conversation(type=1, spawnId=30311, script='$02000230_BF__SAVE_03__1$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=30313, script='$02000230_BF__SAVE_03__2$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 도망과공격()


class 도망과공격(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[300])
        set_actor(triggerId=301, visible=False, initialSequence='Emotion_Failure_Idle_A')
        create_monster(spawnIds=[311], arg2=False)
        set_conversation(type=1, spawnId=311, script='$02000230_BF__SAVE_03__3$', arg4=2, arg5=0)
        move_npc(spawnId=311, patrolName='MS2PatrolData_311_11000689')
        set_conversation(type=1, spawnId=311, script='$02000230_BF__SAVE_03__4$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=90311, spawnIds=[311]):
            return 도망완료()


class 도망완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[311])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[30311,30312,30313,30314,30315]):
            return 트리거초기화()
        if not monster_in_combat(boxIds=[30311,30312,30313,30314,30315]):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=10)
        destroy_monster(spawnIds=[30311,30312,30313,30314,30315])

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 대기()


