""" trigger/02010038_bf/portal01.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=50, visible=False, enabled=False, minimapVisible=False)
        set_actor(triggerId=1000, visible=True, initialSequence='co_functobj_sensor_A01_Off')
        set_interact_object(triggerIds=[10000881], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000881], arg2=0):
            return 이동()


class 이동(state.State):
    def on_enter(self):
        set_portal(portalId=50, visible=False, enabled=True, minimapVisible=False)
        set_actor(triggerId=1000, visible=True, initialSequence='co_functobj_sensor_A01_On')
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            set_portal(portalId=50, visible=False, enabled=False, minimapVisible=False)
            return 재사용대기()


class 재사용대기(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=5)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 대기()


