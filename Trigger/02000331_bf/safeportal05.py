""" trigger/02000331_bf/safeportal05.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=52, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[99994]):
            return 포털작동()


class 포털작동(state.State):
    def on_enter(self):
        set_portal(portalId=52, visible=False, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            return 대기()


