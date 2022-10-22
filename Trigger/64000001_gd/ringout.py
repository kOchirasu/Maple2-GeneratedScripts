""" trigger/64000001_gd/ringout.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_portal(portalId=12, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 링아웃()


class 링아웃(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            move_user(mapId=64000001, portalId=2, boxId=105)
            return 대기()


