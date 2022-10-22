""" trigger/02000088_bf/fruit04.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000141], state=1)
        set_effect(triggerIds=[204], visible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000141], arg2=0):
            return 몬스터리젠()


class 몬스터리젠(state.State):
    def on_enter(self):
        set_effect(triggerIds=[204], visible=False)
        create_monster(spawnIds=[104], arg2=True)
        set_timer(timerId='1', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대화()


class 대화(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=90)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[104]):
            return 트리거초기화()
        if time_expired(timerId='1'):
            return 트리거초기화()


class 트리거초기화(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1)
        destroy_monster(spawnIds=[104])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()

