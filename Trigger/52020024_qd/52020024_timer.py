""" trigger/52020024_qd/52020024_timer.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart', value=1):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=5, startDelay=1, interval=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='TimerStart', value=2)
        self.set_user_value(triggerId=99990003, key='FinalPhase', value=2)
        self.reset_timer(timerId='1')


initial_state = 대기
