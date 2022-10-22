""" trigger/02000066_bf/reward.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[11000011], state=2)
        set_interact_object(triggerIds=[11000012], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return None # Missing State: 생성조건


