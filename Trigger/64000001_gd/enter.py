""" trigger/64000001_gd/enter.xml """
from common import *
import state


class PvP(state.State):
    def on_enter(self):
        set_effect(triggerIds=[701], visible=False)
        set_effect(triggerIds=[702], visible=False)

    def on_tick(self) -> state.State:
        if true():
            set_pvp_zone(boxId=101, arg2=30, duration=120, additionalEffectId=90001002, arg5=4, boxIds=[102,103,112,113,10,11,1,3])
            return PvP종료()


class PvP종료(state.State):
    def on_tick(self) -> state.State:
        if pvp_zone_ended(boxId=101):
            return 게임종료()


class 게임종료(state.State):
    def on_enter(self):
        set_timer(timerId='999', seconds=4, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='999'):
            return 완료()

    def on_exit(self):
        reset_timer(timerId='999')


class 완료(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=60) # action name="포탈을설정한다" arg1="1" arg2="1" arg3="1" arg4="1"/

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            move_user(mapId=0, portalId=0)
            return None


