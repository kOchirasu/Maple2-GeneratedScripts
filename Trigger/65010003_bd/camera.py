""" trigger/65010003_bd/camera.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=101, boxId=2):
            return PvP시작()
        if pvp_zone_ended(boxId=101):
            return 완료()


class PvP시작(state.State):
    def on_enter(self):
        add_buff(boxIds=[101], skillId=70000088, level=1, arg4=False, arg5=False)
        add_buff(boxIds=[101], skillId=70000089, level=1, arg4=False, arg5=False)

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


