""" trigger/02000244_bf/timer.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[798,799], visible=True)
        set_effect(triggerIds=[2001], visible=False)
        set_effect(triggerIds=[2002], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=205, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[205]):
            return 시작()

state.DungeonStart = DungeonStart


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[798,799], visible=False)
        set_timer(timerId='89', seconds=3, clearAtZero=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='89'):
            return 목소리()


class 목소리(state.State):
    def on_enter(self):
        set_effect(triggerIds=[2001], visible=True)
        set_event_ui(type=1, arg2='$02000244_BF__TIMER__0$', arg3='5000', arg4='0')


