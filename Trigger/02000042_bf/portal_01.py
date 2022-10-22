""" trigger/02000042_bf/portal_01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10000583], state=1)
        set_portal(portalId=6, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000583], arg2=0):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=5)
        set_portal(portalId=6, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return 대기()


