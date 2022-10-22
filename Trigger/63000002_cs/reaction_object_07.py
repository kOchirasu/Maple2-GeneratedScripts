""" trigger/63000002_cs/reaction_object_07.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[5001]):
            return 채집가능()


class 채집가능(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[607], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[607], arg2=2):
            create_item(spawnIds=[1007])
            return 채집완료()


class 채집완료(state.State):
    def on_enter(self):
        set_timer(timerId='7', seconds=30, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='7'):
            return 대기()


