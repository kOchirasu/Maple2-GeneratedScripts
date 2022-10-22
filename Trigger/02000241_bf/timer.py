""" trigger/02000241_bf/timer.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2001], visible=False)
        set_effect(triggerIds=[2002], visible=False)
        set_effect(triggerIds=[2003], visible=False)
        set_mesh(triggerIds=[709,710], visible=True)

    def on_tick(self) -> state.State:
        if count_users(boxId=205, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[205]):
            return 어나운스0()

state.DungeonStart = DungeonStart


class 어나운스0(state.State):
    def on_enter(self):
        set_timer(timerId='88', seconds=5, clearAtZero=False)
        set_effect(triggerIds=[2001], visible=True)
        set_event_ui(type=1, arg2='$02000241_BF__TIMER__0$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='88'):
            return 어나운스1()


class 어나운스1(state.State):
    def on_enter(self):
        set_timer(timerId='88', seconds=5, clearAtZero=False)
        set_effect(triggerIds=[2002], visible=True)
        set_event_ui(type=1, arg2='$02000241_BF__TIMER__1$', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if time_expired(timerId='88'):
            return 초재기0()


class 초재기0(state.State):
    def on_enter(self):
        set_timer(timerId='98', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 시작0()


class 시작0(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_timer(timerId='98', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='98'):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_event_ui(type=1, arg2='$02000241_BF__TIMER__4$', arg3='5000', arg4='0')
        set_mesh(triggerIds=[709,710], visible=False)
        set_timer(timerId='44', seconds=6)

    def on_tick(self) -> state.State:
        if time_expired(timerId='44'):
            return 초재기2()


class 초재기2(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='99'):
            return 유저이동음성()


class 유저이동음성(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 유저이동()


class 유저이동(state.State):
    def on_tick(self) -> state.State:
        if true():
            return 끝()


class 끝(state.State):
    pass


