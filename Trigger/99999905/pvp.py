""" trigger/99999905/pvp.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        set_timer(timerId='30', seconds=30, clearAtZero=False)
        set_mesh(triggerIds=[3001,3002,3003,4001,4002,4003], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if count_users(boxId=104, boxId=1):
            return PvP()
        if time_expired(timerId='30'):
            return PvP()


class PvP(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1, clearAtZero=False)
        set_pvp_zone(boxId=104, arg2=3, duration=600, additionalEffectId=90001002, arg5=3, boxIds=[1,2,101,102,103])

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 어나운스0()


class 어나운스0(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2, clearAtZero=False)
        set_event_ui(type=1, arg2='$99999905__PVP__0$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 어나운스1()


class 어나운스1(state.State):
    def on_enter(self):
        set_timer(timerId='4', seconds=4, clearAtZero=False)
        set_event_ui(type=1, arg2='$99999905__PVP__1$', arg3='4000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='4'):
            return 어나운스2()


class 어나운스2(state.State):
    def on_enter(self):
        set_timer(timerId='2', seconds=2, clearAtZero=False)
        set_event_ui(type=1, arg2='$99999905__PVP__2$', arg3='2000')

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 어나운스3()


class 어나운스3(state.State):
    def on_enter(self):
        set_timer(timerId='3', seconds=3, clearAtZero=False)
        show_count_ui(text='$99999905__PVP__3$', stage=1, count=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 문열림()


class 문열림(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            set_mesh(triggerIds=[3001,3002,3003,4001,4002,4003], visible=False, arg3=0, arg4=0, arg5=0)
            return PvP종료()


class PvP종료(state.State):
    def on_tick(self) -> state.State:
        if pvp_zone_ended(boxId=104):
            return 게임종료()


class 게임종료(state.State):
    def on_enter(self):
        set_timer(timerId='10', seconds=10)

    def on_tick(self) -> state.State:
        if time_expired(timerId='10'):
            return None # Missing State: 보상


