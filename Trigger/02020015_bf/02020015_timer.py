""" trigger/02020015_bf/02020015_timer.xml """
import common


class 신호대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Timer', value=1):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=20, startDelay=1, interval=1)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019], visible=False)
        self.reset_timer(timerId='1')


initial_state = 신호대기
