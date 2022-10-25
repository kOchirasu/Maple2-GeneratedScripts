""" trigger/52000014_qd/move_6400.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[6400], enable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9640]):
            return 침몰01(self.ctx)


class 침몰01(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=17)
        self.set_breakable(triggerIds=[6400], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='1'):
            return 대기(self.ctx)


initial_state = 대기
