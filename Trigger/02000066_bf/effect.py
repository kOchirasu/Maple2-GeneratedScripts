""" trigger/02000066_bf/effect.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=False)

    def on_tick(self) -> state.State:
        if npc_detected(boxId=103, spawnIds=[99]):
            return 이펙트생성()


class 이펙트생성(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6001], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[99]):
            return 이펙트소멸()


class 이펙트소멸(state.State):
    def on_enter(self):
        set_timer(timerId='15', seconds=15)
        set_effect(triggerIds=[6001], visible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='15'):
            return 시작()


