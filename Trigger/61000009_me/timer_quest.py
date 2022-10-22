""" trigger/61000009_me/timer_quest.xml """
from common import *
import state


class Ready(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=700, boxId=1):
            return Ready_Idle()


class Ready_Idle(state.State):
    def on_enter(self):
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Ready_Idle_02()


class Ready_Idle_02(state.State):
    def on_enter(self):
        set_timer(timerId='60', seconds=60, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='60'):
            return daily_quest()


class daily_quest(state.State):
    def on_enter(self):
        set_achievement(triggerId=799, type='trigger', achieve='dailyquest_start')


