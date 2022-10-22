""" trigger/02000230_bf/save_07.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        create_monster(spawnIds=[700], arg2=False)
        set_actor(triggerId=701, visible=True, initialSequence='Emotion_Failure_Idle_A')
        set_actor(triggerId=70701, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=70702, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=70703, visible=True, initialSequence='Attack_02_A')
        set_actor(triggerId=70704, visible=True, initialSequence='Attack_Idle_A')
        set_actor(triggerId=70705, visible=True, initialSequence='Attack_02_A')

    def on_tick(self) -> state.State:
        if true():
            return 주민구출()


class 주민구출(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000359], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000359], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=3)
        set_conversation(type=1, spawnId=700, script='$02000230_BF__SAVE_07__0$', arg4=2, arg5=0)
        set_actor(triggerId=70701, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[70711], arg2=True)
        set_actor(triggerId=70702, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[70712], arg2=True)
        set_actor(triggerId=70703, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[70713], arg2=True)
        set_actor(triggerId=70704, visible=False, initialSequence='Attack_Idle_A')
        create_monster(spawnIds=[70714], arg2=True)
        set_actor(triggerId=70705, visible=False, initialSequence='Attack_02_A')
        create_monster(spawnIds=[70715], arg2=True)
        set_conversation(type=1, spawnId=70711, script='$02000230_BF__SAVE_07__1$', arg4=2, arg5=1)
        set_conversation(type=1, spawnId=70713, script='$02000230_BF__SAVE_07__2$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 도망과공격()


class 도망과공격(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[700])
        set_actor(triggerId=701, visible=False, initialSequence='Emotion_Failure_Idle_A')
        create_monster(spawnIds=[711], arg2=False)
        set_conversation(type=1, spawnId=711, script='$02000230_BF__SAVE_07__3$', arg4=2, arg5=0)
        move_npc(spawnId=711, patrolName='MS2PatrolData_711_11000687')
        set_conversation(type=1, spawnId=711, script='$02000230_BF__SAVE_07__4$', arg4=2, arg5=2)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=90711, spawnIds=[711]):
            return 도망완료()


class 도망완료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[711])

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[70711,70712,70713,70714,70715]):
            return 트리거초기화()
        if not monster_in_combat(boxIds=[70711,70712,70713,70714,70715]):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='11', seconds=10)
        destroy_monster(spawnIds=[70711,70712,70713,70714,70715])

    def on_tick(self) -> state.State:
        if time_expired(timerId='11'):
            return 대기()


