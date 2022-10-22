""" trigger/02000110_bf/01_triggermodel01_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000064], state=1)
        set_actor(triggerId=11, visible=True, initialSequence='Closed')
        set_effect(triggerIds=[202], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000064], arg2=0):
            return 몬스터와전투()


class 몬스터와전투(state.State):
    def on_enter(self):
        set_actor(triggerId=11, visible=True, initialSequence='Opened')
        create_monster(spawnIds=[102], arg2=True)
        set_effect(triggerIds=[202], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 몬스터전투()


class 몬스터전투(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[102]):
            return 트리거초기화()
        if not monster_in_combat(boxIds=[102]):
            return 몬스터소멸()


class 몬스터소멸(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=30)

    def on_tick(self) -> state.State:
        if monster_in_combat(boxIds=[102]):
            reset_timer(timerId='1')
            return None
        if monster_dead(boxIds=[102]):
            return 소멸대기()
        if time_expired(timerId='1'):
            return 소멸대기()


class 소멸대기(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 트리거초기화()
        if monster_in_combat(boxIds=[102]):
            return 몬스터소멸()


class 트리거초기화(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        set_timer(timerId='2', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()

    def on_exit(self):
        reset_timer(timerId='2')


