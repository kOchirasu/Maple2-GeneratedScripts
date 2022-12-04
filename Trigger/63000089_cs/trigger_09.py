""" trigger/63000089_cs/trigger_09.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[309], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[109]):
            return 발판09(self.ctx)


class 발판09(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[309], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[109]):
            return 발판09끝(self.ctx)


class 발판09끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='409', seconds=2, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='409'):
            return 대기(self.ctx)


initial_state = 대기
