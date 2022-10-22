""" trigger/02000169_bf/opendoor_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000381], state=1)
        set_portal(portalId=10, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000381], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=10)
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


