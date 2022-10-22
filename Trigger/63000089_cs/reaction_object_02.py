""" trigger/63000089_cs/reaction_object_02.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[5001]):
            return 채집가능()


class 채집가능(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[602], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[602], arg2=2):
            create_item(spawnIds=[1002])
            return 채집완료()


class 채집완료(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()


