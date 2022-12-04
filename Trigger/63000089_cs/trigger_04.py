""" trigger/63000089_cs/trigger_04.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[304], visible=False, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return 발판04(self.ctx)


class 발판04(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[304], visible=True, arg3=0, delay=0, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[104]):
            return 발판04끝(self.ctx)


class 발판04끝(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='404', seconds=2, startDelay=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='404'):
            return 대기(self.ctx)


initial_state = 대기
