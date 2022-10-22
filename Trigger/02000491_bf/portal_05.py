""" trigger/02000491_bf/portal_05.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=805, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000987], arg2=0):
            return 포털활성화()


class 포털활성화(state.State):
    def on_enter(self):
        set_portal(portalId=805, visible=False, enabled=True, minimapVisible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            set_interact_object(triggerIds=[10000987], state=1)
            return 대기()


class 종료(state.State):
    pass


