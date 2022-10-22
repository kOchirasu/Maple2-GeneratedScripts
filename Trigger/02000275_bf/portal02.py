""" trigger/02000275_bf/portal02.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=52, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10000699], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000699], arg2=0):
            return 생성()


class 생성(state.State):
    def on_enter(self):
        set_portal(portalId=52, visible=False, enabled=True, minimapVisible=False)
        set_timer(timerId='2', seconds=2, clearAtZero=False, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            set_portal(portalId=52, visible=False, enabled=False, minimapVisible=False)
            return 재사용대기()


class 재사용대기(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, clearAtZero=False, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 대기()


