""" trigger/02000241_bf/timer.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[2001], visible=False)
        self.set_effect(triggerIds=[2002], visible=False)
        self.set_effect(triggerIds=[2003], visible=False)
        self.set_mesh(triggerIds=[709,710], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=205, boxId=1):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[205]):
            return 어나운스0(self.ctx)


class 어나운스0(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='88', seconds=5, startDelay=0)
        self.set_effect(triggerIds=[2001], visible=True)
        self.set_event_ui(type=1, arg2='$02000241_BF__TIMER__0$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='88'):
            return 어나운스1(self.ctx)


class 어나운스1(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='88', seconds=5, startDelay=0)
        self.set_effect(triggerIds=[2002], visible=True)
        self.set_event_ui(type=1, arg2='$02000241_BF__TIMER__1$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='88'):
            return 초재기0(self.ctx)


class 초재기0(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='98', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='98'):
            return 시작0(self.ctx)


class 시작0(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_timer(timerId='98', seconds=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='98'):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_event_ui(type=1, arg2='$02000241_BF__TIMER__4$', arg3='5000', arg4='0')
        self.set_mesh(triggerIds=[709,710], visible=False)
        self.set_timer(timerId='44', seconds=6)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='44'):
            return 초재기2(self.ctx)


class 초재기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='99'):
            return 유저이동음성(self.ctx)


class 유저이동음성(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 유저이동(self.ctx)


class 유저이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 끝(self.ctx)


class 끝(trigger_api.Trigger):
    pass


initial_state = idle
