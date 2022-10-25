""" trigger/02000347_bf/guide.xml """
import common


class 대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[60002]):
            return 대기_02(self.ctx)


class 대기_02(common.Trigger):
    def on_enter(self):
        self.set_timer(timerId='8', seconds=8)

    def on_tick(self) -> common.Trigger:
        if self.time_expired(timerId='8'):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02000347_BF__MAIN1__5$', arg3='5000', arg4='0')


initial_state = 대기
