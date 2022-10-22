""" trigger/02000277_bf/portal_02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000631], state=1)
        set_portal(portalId=50, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000631], arg2=0):
            return 문열림()


class 문열림(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=7)
        set_portal(portalId=50, visible=True, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 대기()


