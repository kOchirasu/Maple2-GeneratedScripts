""" trigger/61000009_me/timer_quest.xml """
import common


class Ready(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=700, boxId=1):
            return Ready_Idle(self.ctx)


class Ready_Idle(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return Ready_Idle_02(self.ctx)


class Ready_Idle_02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='60', seconds=60, interval=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='60'):
            return daily_quest(self.ctx)


class daily_quest(common.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=799, type='trigger', achieve='dailyquest_start')


initial_state = Ready
