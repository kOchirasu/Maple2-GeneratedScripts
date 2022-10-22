""" trigger/02000066_bf/q10003067.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[103], questIds=[50001642], questStates=[2]):
            return 포털활성화()


class 포털활성화(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='woodsoflife', value=1):
            return None # Missing State: 포털비활성화


class 가이드활성화(state.State):
    def on_enter(self):
        guide_event(eventId=10003067)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 종료()


class 종료(state.State):
    pass


