""" trigger/02000066_bf/cannon_effect16.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[816], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[126]):
            return 이펙트대기()


class 이펙트대기(state.State):
    def on_tick(self) -> state.State:
        if npc_detected(boxId=126, spawnIds=[8016]):
            return 이펙트on()


class 이펙트on(state.State):
    def on_enter(self):
        set_effect(triggerIds=[816], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[8016]):
            return 대기시간()
        if not user_detected(boxIds=[126]):
            return 대기시간()


class 대기시간(state.State):
    def on_enter(self):
        set_effect(triggerIds=[816], visible=False)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 시작()


