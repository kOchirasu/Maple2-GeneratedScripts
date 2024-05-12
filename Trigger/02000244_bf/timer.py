""" trigger/02000244_bf/timer.xml """
import trigger_api

#include dungeon_common/checkusercount.py
from dungeon_common.checkusercount import *


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[798,799], visible=True)
        self.set_effect(trigger_ids=[2001], visible=False)
        self.set_effect(trigger_ids=[2002], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(box_id=205, min_users='1'):
            return CheckUserCount(self.ctx)


class DungeonStart(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(box_ids=[205]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(trigger_ids=[798,799], visible=False)
        self.set_timer(timer_id='89', seconds=3, start_delay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timer_id='89'):
            return 목소리(self.ctx)


class 목소리(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(trigger_ids=[2001], visible=True)
        self.set_event_ui(type=1, arg2='$02000244_BF__TIMER__0$', arg3='5000', arg4='0')


initial_state = 대기
