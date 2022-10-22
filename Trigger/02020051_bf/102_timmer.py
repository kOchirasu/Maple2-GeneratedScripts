""" trigger/02020051_bf/102_timmer.xml """
from common import *
import state


class 시작(state.State):
    def on_enter(self):
        reset_timer(timerId='990')

    def on_tick(self) -> state.State:
        if user_value(key='Timmer', value=1):
            return 타이머()


class 타이머(state.State):
    def on_enter(self):
        set_timer(timerId='990', seconds=600, clearAtZero=True, display=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=600000):
            return 종료()
        if user_value(key='Timmer', value=3):
            return 시작()


class 종료(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_shy', script='$02020051_BF__102_TIMMER__0$', duration=5684, voice='ko/Npc/00002201')
        set_user_value(triggerId=104, key='End', value=3)

    def on_tick(self) -> state.State:
        if user_value(key='Timmer', value=2):
            return 시작()


