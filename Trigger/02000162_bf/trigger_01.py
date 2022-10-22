""" trigger/02000162_bf/trigger_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000275], state=1)
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158], visible=True)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000275], arg2=0):
            return 용암()


class 용암(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158], visible=False)
        set_timer(timerId='1', seconds=100)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()
        if quest_user_detected(boxIds=[201], questIds=[20001290], questStates=[2]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=20)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 대기()


