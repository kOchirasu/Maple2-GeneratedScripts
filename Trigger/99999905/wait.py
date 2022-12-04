""" trigger/99999905/wait.xml """
import trigger_api


class 시간표확인(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='10', seconds=10, startDelay=0)
        self.set_event_ui(type=1, arg2='$99999905__WAIT__0$', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=101, boxId=10):
            return 시작(self.ctx)
        if self.time_expired(timerId='10'):
            return 시간표확인(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='88', seconds=1200, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='88'):
            return 시간표확인(self.ctx)


initial_state = 시간표확인
