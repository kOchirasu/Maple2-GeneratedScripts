""" trigger/64000001_gd/wait.xml """
import common


class 시간표확인(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=10, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.count_users(boxId=104, boxId=6):
            return 시작(self.ctx)
        if self.time_expired(timerId='10'):
            return 시간표확인(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='88', seconds=1200, startDelay=0)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='88'):
            return 시간표확인(self.ctx)


initial_state = 시간표확인
