""" trigger/65010001_bd/camera.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[101]):
            return PvP종료()


class PvP종료(state.State):
    def on_tick(self) -> state.State:
        if pvp_zone_ended(boxId=101):
            return 완료()


class 완료(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=15000):
            move_user(mapId=0, portalId=0)
            return 종료()


class 종료(state.State):
    pass


