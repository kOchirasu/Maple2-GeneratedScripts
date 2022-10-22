""" trigger/02000254_bf/karl.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_effect(triggerIds=[450], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[904]):
            return 말풍선()
        if monster_in_combat(boxIds=[106]):
            return 종료()


class 말풍선(state.State):
    def on_enter(self):
        set_timer(timerId='8', seconds=8)
        set_effect(triggerIds=[450], visible=True)
        set_conversation(type=1, spawnId=107, script='$02000254_BF__KARL__0$', arg4=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='8'):
            return 시작()


class 종료(state.State):
    pass


