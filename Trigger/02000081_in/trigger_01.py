""" trigger/02000081_in/trigger_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000384], state=1)
        destroy_monster(spawnIds=[201])
        set_mesh(triggerIds=[101,102,103,104], visible=False)
        set_actor(triggerId=501, visible=True, initialSequence='Opened')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000384], arg2=0):
            return 닫히기()


class 닫히기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101,102,103,104], visible=True)
        set_actor(triggerId=501, visible=True, initialSequence='Closed')
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 토무등장()


class 토무등장(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=True)
        move_npc(spawnId=202, patrolName='MS2PatrolData_202')

    def on_tick(self) -> state.State:
        if npc_detected(boxId=402, spawnIds=[202]):
            return 토무대사()


class 토무대사(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=202, script='$02000081_IN__TRIGGER_01__0$', arg4=4)
        set_timer(timerId='1', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 토무대사2()


class 토무대사2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=202, script='$02000081_IN__TRIGGER_01__1$', arg4=4)
        set_timer(timerId='1', seconds=4)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 토무대사3()


class 토무대사3(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=202, script='$02000081_IN__TRIGGER_01__2$', arg4=2)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 변신()


class 변신(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[201], arg2=True)
        set_actor(triggerId=501, visible=True, initialSequence='Opened')
        set_mesh(triggerIds=[101,102,103,104], visible=False)

    def on_tick(self) -> state.State:
        if true():
            return 몬스터와전투()


class 몬스터와전투(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[201]):
            return 대기()
        if not monster_in_combat(boxIds=[201]):
            return 토무소멸()


class 토무소멸(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=20)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[201]):
            reset_timer(timerId='1')
            return None
        if monster_dead(boxIds=[201]):
            return 대기()
        if time_expired(timerId='1'):
            return 소멸대기()


class 소멸대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 트리거초기화()
        if monster_in_combat(boxIds=[201]):
            return 토무소멸()


class 트리거초기화(state.State):
    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[201]):
            return 토무소멸()
        if not monster_in_combat(boxIds=[201]):
            destroy_monster(spawnIds=[201])
            return 대기()


