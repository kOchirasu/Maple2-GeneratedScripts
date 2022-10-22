""" trigger/02020112_bf/safezone2.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990017, key='Safe', value=0)
        set_interact_object(triggerIds=[10002118], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[903], jobCode=0):
            return 안전장치_활성화()


class 안전장치_활성화(state.State):
    def on_enter(self):
        set_portal(portalId=8, visible=True, enabled=True, minimapVisible=False)
        set_portal(portalId=10, visible=True, enabled=True, minimapVisible=False)
        set_interact_object(triggerIds=[10002118], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002118], arg2=0):
            return 안전장치_작동()


class 안전장치_작동(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020112_BF__SAFEZONE2__0$', arg3='5000')
        set_user_value(triggerId=99990017, key='Safe', value=1)


